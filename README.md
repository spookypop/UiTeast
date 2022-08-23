# UiTeast
web自动化测试实践PO模式
<p>使用selenium官网推荐的最佳实践PO(page object)模式，就是将测试代码与页面定位代码分离。当页面元素发生变化时只需要改定位代码，测试用例本身是不需要更改的。</p>
<p>比如写登录功能的自动化测试代码，将页面的元素定位和该页面提供的方法放在独立的一个类中（Pages->LoginPage.py），登录的用例代码单独一个类（Testcase->LoginCase.py）</p>
<p>运行main.py文件之前安装必要的依赖</p>
<p>pip install selenium</p>
<p>pip install webdriver-manager</p>
