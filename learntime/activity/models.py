import uuid
from datetime import datetime

from django.conf import settings
from django.db import models

from learntime.DjangoUeditor.models import UEditorField
from learntime.utils.models import CreatedUpdatedMixin


class Activity(CreatedUpdatedMixin, models.Model):
    """活动表"""

    TYPE = (
        ("n", "未选择"),
        ("fl_credit", "法律"),
        ("wt_credit", "文体"),
        ("xl_credit", "心理"),
        ("cxcy_credit", "创新创业"),
        ("sxdd_credit", "思想道德"),
    )

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True,
                           editable=False, verbose_name="活动id")
    name = models.CharField(max_length=255, verbose_name="活动名称")
    desc = UEditorField(verbose_name='活动内容', imagePath='activity/images/%Y/%m/%d/', width=800, height=350,
                        filePath='activity/files/%Y/%m/%d/', default='')
    score_player = models.FloatField(default=0, verbose_name="参与者学时")
    score_staff = models.FloatField(default=0, verbose_name="工作人员学时")
    score_viewer = models.FloatField(default=0, verbose_name="观众学时")
    sponsor = models.CharField(verbose_name="组织方", max_length=255)
    time = models.DateTimeField(default=datetime.now, verbose_name="活动时间")
    credit_type = models.CharField(choices=TYPE, max_length=20, verbose_name="学时类别",
                                   default="n")
    file = models.FileField(upload_to="activity/%Y/%m/%d/", verbose_name="活动策划表",
                            null=True, blank=True)
    is_verify = models.BooleanField(verbose_name="是否通过审核", default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name="发布者", null=True, blank=True)

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = verbose_name
        db_table = "activity"


    def __str__(self):
        return self.name
