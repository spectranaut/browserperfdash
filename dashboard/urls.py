from django.conf.urls import include, url
from dashboard.views import *
from . import views

urlpatterns = [
    url(r'^bot-report', BotReportView.as_view()),
    url(r'^browser_results_exist/$', BrowsersForResultsExistList.as_view()),
    url(r'^bot/$', BotsList.as_view(), name='bots-list'),
    url(r'^bot/detail/(?P<pk>\w+)$', BotDetailView.as_view()),
    url(r'^platform/$', PlatformList.as_view(), name='platform-list'),
    url(r'^gpu/$', GPUTypeList.as_view(), name='gputype-list'),
    url(r'^cpu/$', CPUArchitectureList.as_view(), name='cpuarch-list'),
    url(r'^test/$', TestList.as_view(), name='test-list'),
    url(r'^bot_results_exist/(?P<browser>.+)$', BotsForResultsExistList.as_view()),
    url(r'^testpath/(?P<browser>.+)/(?P<test>.+)$', TestPathList.as_view()),
    url(r'^test_metrics/(?P<test>[-\w]+)/(?P<subtest>.+)$', MetricsForTestList.as_view()),
    url(r'^tests_for_browser_bot/(?P<browser>.+)/(?P<bot>.*)$', TestsForBrowserBotList.as_view()),
    url(r'^results_for_subtest/(?P<browser>[-\w]+)/(?P<test>[-\w]+)/(?P<bot>[-\w]+)/(?P<subtest>.+)/$',
        ResultsForSubtestList.as_view()),
    url(r'^report/detail/(?P<pk>\d+)$', BotDataReportDetailView.as_view()),
    url(r'^report/test/(?P<pk>\d+)$', BotResultsForTestListView.as_view()),
    url(r'^report/improvement/(?P<days_since>\d+)/(?P<platform>[-\w]+)/(?P<gpu>[-\w]+)/'
        r'(?P<cpu>[-\w]+)/(?P<browser>[-\w]+)/(?P<test>[-\w]+)/(?P<bot>[-\w]+)/(?P<limit>\d+)/$',
        BotDataReportImprovementListView.as_view()),
    url(r'^report/regression/(?P<days_since>\d+)/(?P<platform>[-\w]+)/(?P<gpu>[-\w]+)/'
        r'(?P<cpu>[-\w]+)/(?P<browser>[-\w]+)/(?P<test>[-\w]+)/(?P<bot>[-\w]+)/(?P<limit>\d+)/$',
        BotDataReportRegressionListView.as_view()),
    url(r'^report_full/$', BotDataCompleteListView.as_view()),
    url(r'^graph/$', GraphPlotView.as_view(), name='graph_report')
]