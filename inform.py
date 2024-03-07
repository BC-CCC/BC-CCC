# inform.py

class Inform:
    @staticmethod
    def get_analyst_output(results):
        # 根据六次投掷结果综合输出内容
        # 这里根据你的要求进行修改
        if results == ['little yin','little yin','little yin','little yin','little yin','little yin'] :
            return "Go with the flow"
        elif results == ['little yang','little yin','little yin','little yin','little yin','little yin']:
            return "Moving in the right direction"
        
        else:
            return "Custom Analyst Output"