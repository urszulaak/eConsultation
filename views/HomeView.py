from views.View import View

class HomeView(View):

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller
    #     self._openCmd()

    # def _openCmd(self):
    #     os.system("ls")

    def main(self):
        print("Hello world")
        
    def close(self):
        return
    
