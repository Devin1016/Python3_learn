class AI:
    def face_recongnition(self):
        print('人脸识别')

    def data_handle(self):
        print('AI数据处理')


class BigData:
    def data_analysis(self):
        print('数据分析')

    def data_handle(self):
        print('BigData数据处理')


class Python(AI, BigData):
    def operation(self):
        print('自动化运维')


py = Python()
py.face_recongnition()
py.data_analysis()
py.operation()
py.data_handle()
