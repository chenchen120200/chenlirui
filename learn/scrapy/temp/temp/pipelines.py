# �����ﶨ�����Item����ܵ�
#
# ��Ҫ���ǽ��ܵ���ӵ�ITEM_PIPELINES������
# �ο���https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# ����ʹ�õ�һ�ӿڴ���ͬ����Item��ģ��
from itemadapter import ItemAdapter


class TempPipeline:
    def process_item(self, item, spider):
        return item
