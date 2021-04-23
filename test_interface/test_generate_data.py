import pytest


class TestGenerateData:
    """
    七点法生成七个边界值数据
    """

    @pytest.mark.parametrize("left, right", [[1, 8], [1, 9]])
    def test_boundary_data(self, left: int, right: int, pre: int = 1) -> list:
        """
        :param left: 左边界，参数的类型为int
        :param right: 右边界，参数的类型为int
        :param pre: 精度，参数的类型为1，默认为1
        :return: 返回值的类型为list
        """
        if isinstance(left, int) and isinstance(right, int) and isinstance(pre, int):
            result = []
            lefts = [left - pre, left, left + pre]
            rights = [right - pre, right, right + pre]
            mid = (left + right) // 2
            result.extend(lefts)
            result.append(mid)
            result.extend(rights)
            return result
        else:
            raise ValueError("请检查参数的类型！")
