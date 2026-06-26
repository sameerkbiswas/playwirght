cd /Volumes/SKB/Development/Python3/workspaces/Playwright/BDD_Playwright/features

$ behave --tags=@run
$ behave --tags=~@run
$ behave --tags=@register
$ behave --tags=~@register
$ behave --tags=~@register | @run
$ behave --tags=@register | @run
$ behave --tags=@register or @run
$ behave --tags=@register || @run