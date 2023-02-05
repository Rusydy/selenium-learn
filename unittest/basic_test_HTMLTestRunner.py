import unittest
import HTMLTestRunner

#测试用例, en: test case

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testCase1(self):
        self.assertEqual(2,2,"testError")

    # The following test case will fail
    def testCase2(self):
        self.assertEqual(2,3,"testError")

    def testCase3(self):
        self.assertEqual(2,5,"测试错误")  # en: test error

    def testCase4(self):
        self.assertEqual(2,1,"测试错误")
    # The upper test case will fail
    
    def testCase5(self):
        pass

class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(2, 2, "testError")

    def testCase2(self):
        self.assertEqual(3, 3, "testError")

    def testCase3(self):
        self.assertEqual(5, 5, "testError")

    # the following test case will fail
    def testCase4(self):
        self.assertEqual(2, 1, "测试错误")

    def testCase5(self):
        self.assertEqual(2, 6, "testError")
    # The upper test case will fail
    
    def testCase6(self):
        pass

# 添加Suite, en: add Suite
def Suite():

    #定义一个单元测试容器, en: define a unit test container
    suiteTest = unittest.TestSuite()

    #将测试用例加入到容器, en: add test cases to the container
    suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(MyTestCase("testCase2"))
    suiteTest.addTest(MyTestCase("testCase3"))
    suiteTest.addTest(MyTestCase("testCase4"))
    suiteTest.addTest(MyTestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase1"))
    suiteTest.addTest(APITestCase("testCase2"))
    suiteTest.addTest(APITestCase("testCase3"))
    suiteTest.addTest(APITestCase("testCase4"))
    suiteTest.addTest(APITestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase6"))
    return suiteTest

if __name__ == '__main__':
    with open('report.html', 'w') as f: 
        # open have two parameters, the first is the file name, the second is the mode. 'w' means write, 'r' means read, 'a' means append, 'b' means binary
        runner = HTMLTestRunner.HTMLTestRunner( # type: ignore
            stream=f, # this means the test result will be written to the file
            title='测试报告', # en: test report
            description='测试报告') # en: test report
        unittest.main(testRunner=runner)