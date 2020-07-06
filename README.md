#依赖环境：
win10

python3

pycharm

-----
#目录：
1.base：元素定位封装

2.page：页面层，页面元素封装

3.handle：控制层，元素控制（点击、输入、清空、获取）

4.business：业务层，测试步骤

5.case：调用业务层

6.util：读取excel文件、读取ini配置文件

7.config：元素定位路径ini配置文件、excel测试数据文件

---
#开发流程：

1.页面元素封装到LoacalElement.ini文件中

2.page调用find_element类获取页面元素

3.handle调用page操作元素

4.business调用handle执行测试步骤

5.case调用business层，判断测试结果、截图、生成测试报告