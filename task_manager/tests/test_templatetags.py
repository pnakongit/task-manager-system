from django.test import RequestFactory, TestCase

from task_manager.templatetags.query_transform import query_transform


class QueryTransformTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_without_request_get_parameter(self) -> None:
        request = self.factory.get("/")

        expected_result = "test=2"
        self.assertEqual(query_transform(request, test="2"), expected_result)

    def test_with_request_get_parameter_and_kwarg_argument(self) -> None:
        request = self.factory.get("/?first=1")

        expected_result = "first=1&second=2"
        self.assertEqual(query_transform(request, second="2"), expected_result)

    def test_override_existing_get_parameter(self) -> None:
        request = self.factory.get("/?test=1")

        expected_result = "test=4"
        self.assertEqual(query_transform(request, test="4"), expected_result)

    def test_delete_existing_get_parameter(self) -> None:
        request = self.factory.get("/?test=1")

        expected_result = ""
        self.assertEqual(query_transform(request, test=None), expected_result)

    def test_remove_page_from_get_parameter_if_remove_page_is_true(self) -> None:
        request = self.factory.get("/?page=1")

        expected_result = "test=4"
        self.assertEqual(query_transform(request, remove_page=True, test="4"), expected_result)

    def test_does_not_remove_page_from_get_if_remove_page_is_false(self) -> None:
        request = self.factory.get("/?page=1")

        expected_result = "page=1&test=4"
        self.assertEqual(query_transform(request, test="4"), expected_result)
