
from pynag import Model


def update_host(target_id, charm_cfg):
    host = Model.Host()
    host.set_filename(charm_cfg)
    host.set_attribute('host_name', target_id)
    host.set_attribute('use', 'generic-host')
    # Adding the windows icon image definitions to the host.
    host.set_attribute('icon_image', 'base/win40.png')
    host.set_attribute('icon_image_alt', 'Windows')
    host.set_attribute('vrml_image', 'win40.png')
    host.set_attribute('statusmap_image', 'base/win40.gd2')
    host.save()
    host = Model.Host.objects.get_by_shortname(target_id)
    return host
