#依赖环境：
winAll

python3环境傻瓜式安装（https://www.python.org/）

pycharm编译器傻瓜式安装（http://www.jetbrains.com/pycharm/download/#section=windows）

下载对应浏览器版本的驱动，放置python安装目录（https://www.jianshu.com/p/72eb6c5c6790）

-----

#目录：
1.base：元素定位封装

2.page：页面层，页面元素封装

3.handle：控制层，元素控制（点击、输入、清空、获取）

4.business：业务层，测试步骤

5.case：调用业务层，完成整个case，生成自动化测试报告、截图

6.util：读取excel文件、读取ini配置文件

7.config：元素定位路径ini配置文件、excel测试数据文件

---

#开发流程：

1.页面元素封装到LoacalElement.ini文件中

2.page调用find_element类获取页面元素，封装页面原元素

3.handle调用page层，封装page层的元素操作

4.business调用handle，封装case所有需要的执行操作和步骤

5.case调用business层，调用excel数据驱动，完成case封装，以及判断测试结果、截图、生成测试报告

6.run.py文件用于执行全部case层文件（不需要改动）

#运行

1.导入项目‘kuban’

2.在config文件夹下，编辑excel文件（文件对应case名称，即测试数据）

    2.1.文件名名不限制，但一定要能区分开，内容格式设置为‘文本’

3.运行run.py文件（注意：必须用python运行脚本，不可用unittest运行，否则运行失败）

    3.1.准对单个case单独调试，不要用run.py

4.测试报告在report文件中

    4.1.html格式文件，浏览器中打开查看

5.错误截图在img文件中

    5.1.正确不截图