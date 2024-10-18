import importlib

class Core:    
    def openController(controller):
        response = None

        controllerName = controller[0].upper()+controller[1:]+"Controller"
        module = importlib.import_module("controllers."+controllerName)
        class_ = getattr(module, controllerName)
        response = class_()

        return response;