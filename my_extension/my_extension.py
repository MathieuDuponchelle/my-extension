from hotdoc.core.extension import Extension

class MyExtension(Extension):
    extension_name = 'my-extension'
    argument_prefix = 'my'

    def setup(self):
        print ("Setting up")
        super().setup()

    def parse_config(self, config):
        super().parse_config(config)

def get_extension_classes():
    return [MyExtension]
