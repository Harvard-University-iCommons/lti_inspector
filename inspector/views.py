# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from lti import ToolConfig
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

VARIABLE_EXPANSIONS = [
    'com.instructure.OriginalityReport.id',
    'com.instructure.Submission.id',
    'com.instructure.File.id',
    'CourseOffering.sourcedId',
    'Context.id',
    'Context.sourcedId',
    'Message.documentTarget',
    'Message.locale',
    'ToolConsumerInstance.guid',
    'Canvas.api.domain',
    'Canvas.api.collaborationMembers.url',
    'Canvas.api.baseUrl',
    'ToolProxyBinding.memberships.url',
    'Canvas.account.id',
    'Canvas.account.name',
    'Canvas.account.sisSourceId',
    'Canvas.rootAccount.id',
    'Canvas.rootAccount.sisSourceId',
    'Canvas.externalTool.url',
    'Canvas.css.common',
    'Canvas.shard.id',
    'Canvas.root_account.global_id',
    'Canvas.root_account.id',
    'vnd.Canvas.root_account.uuid',
    'Canvas.root_account.sisSourceId',
    'Canvas.course.id',
    'vnd.instructure.Course.uuid',
    'Canvas.course.name',
    'Canvas.course.sisSourceId',
    'Canvas.course.startAt',
    'Canvas.course.workflowState',
    'Canvas.term.startAt',
    'CourseSection.sourcedId',
    'Canvas.enrollment.enrollmentState',
    'Canvas.membership.roles',
    'Canvas.membership.concludedRoles',
    'Canvas.course.previousContextIds',
    'Canvas.course.previousCourseIds',
    'Person.name.full',
    'Person.name.family',
    'Person.name.given',
    'Person.email.primary',
    'vnd.Canvas.Person.email.sis',
    'Person.address.timezone',
    'User.image',
    'User.id',
    'Canvas.user.id',
    'vnd.instructure.User.uuid',
    'Canvas.user.prefersHighContrast',
    'Canvas.group.contextIds',
    'Membership.role',
    'Canvas.xuser.allRoles',
    'Canvas.user.globalId',
    'Canvas.user.isRootAccountAdmin',
    'User.username',
    'Canvas.user.loginId',
    'Canvas.user.sisSourceId',
    'Canvas.user.sisIntegrationId',
    'Person.sourcedId',
    'Canvas.logoutService.url',
    'Canvas.masqueradingUser.id',
    'Canvas.masqueradingUser.userId',
    'Canvas.xapi.url',
    'Caliper.url',
    'Canvas.course.sectionIds',
    'Canvas.course.sectionSisSourceIds',
    'com.instructure.contextLabel',
    'Canvas.module.id',
    'Canvas.moduleItem.id',
    'Canvas.assignment.id',
    'Canvas.assignment.title',
    'Canvas.assignment.pointsPossible',
    'Canvas.assignment.unlockAt',
    'Canvas.assignment.lockAt',
    'Canvas.assignment.dueAt',
    'Canvas.assignment.unlockAt.iso8601',
    'Canvas.assignment.lockAt.iso8601',
    'Canvas.assignment.dueAt.iso8601',
    'Canvas.assignment.published',
    'LtiLink.custom.url',
    'ToolProxyBinding.custom.url',
    'ToolProxy.custom.url',
    'ToolConsumerProfile.url',
    'Canvas.file.media.id',
    'Canvas.file.media.type',
    'Canvas.file.media.duration',
    'Canvas.file.media.size',
    'Canvas.file.media.title',
    'Canvas.file.usageRights.name',
    'Canvas.file.usageRights.url',
    'Canvas.file.usageRights.copyrightText',
]


def tool_config(request):

    # basic stuff
    app_title = 'LTI Inspector'
    app_description = 'A simple LTI App that echoes the launch parameters'
    launch_view_name = 'lti_launch'
    launch_url = request.build_absolute_uri(reverse(launch_view_name))

    # maybe you've got some extensions
    extensions = {
        'canvas.instructure.com': {
            # extension settings...
            'privacy_level': 'public',
            'custom_fields': {},
            'course_navigation': {
                'url': launch_url,
                'text': app_title,
                'visibility': 'public',
                'default': 'enabled',
                'enabled': 'false',
            }
        }
    }

    for varname in VARIABLE_EXPANSIONS:
        extensions['canvas.instructure.com']['custom_fields'][varname] = '${}'.format(varname)

    lti_tool_config = ToolConfig(
        title=app_title,
        launch_url=launch_url,
        secure_launch_url=launch_url,
        extensions=extensions,
        description=app_description
    )

    return HttpResponse(lti_tool_config.to_xml(), content_type='text/xml')


@xframe_options_exempt
@csrf_exempt
def lti_launch(request):
    context = {}

    return render(request, 'inspector/lti_launch.html', context)
