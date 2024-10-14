from core.Core import Core

class Main:
    def run():
            app = Core.openController("home")
            app.main()

if __name__ == '__main__':
    Main.run()