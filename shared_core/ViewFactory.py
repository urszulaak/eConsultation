import importlib


class ViewFactory:
    _mode = "console"

    @staticmethod
    def set_mode(mode):
        ViewFactory._mode = mode

    @staticmethod
    def load_view(view_name, controller, optional_param=None):
        view_class_name = view_name[0].upper() + view_name[1:] + "View"

        if ViewFactory._mode == "gui":
            module_name = "gui_views." + view_class_name
        else:
            module_name = "views." + view_class_name


        module = importlib.import_module(module_name)
        view_class = getattr(module, view_class_name)

        return view_class(controller, optional_param)