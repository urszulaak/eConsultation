import importlib

class Core:    
    def openController(controller, optional_param=None):
        response = None

        controllerName = controller[0].upper()+controller[1:]+"Controller"
        module = importlib.import_module("shared_core.controllers."+controllerName)
        class_ = getattr(module, controllerName)
        response = class_(optional_param)

        return response