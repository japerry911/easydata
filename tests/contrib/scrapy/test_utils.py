import json

from easydata.contrib.scrapy.utils import response_to_data_bag
from tests.factory.scrapy import fake_response


def test_response_to_data_bag():
    data = response_to_data_bag(fake_response(body=json.dumps({"name": "Easybook 15"})))

    assert json.loads(data["main"]) == {"name": "Easybook 15"}


def test_response_to_data_bag_with_cb_kwargs():
    data = response_to_data_bag(
        fake_response(body=json.dumps({"name": "Easybook 15"})),
        brand_info={"name": "EasyData"},
        empty_info=None,
    )

    assert json.loads(data["main"]) == {"name": "Easybook 15"}

    assert data["brand_info"] == {"name": "EasyData"}

    assert data["empty_info"] is None
