from models.suite_config import RunConfig


class MobileDevices:

    ANDROID_5 = RunConfig(browser= "android", device_name = "Android 5.1 Emulator")

    NEXUS_4 = RunConfig(browser= "android", device_name = "LG Nexus 4 Emulator")

    SAMSUNG_GALAXY_TAB_3 = RunConfig(browser= "android", device_name = "Samsung Galaxy Tab 3 Emulator")

    NEXUS_7 = RunConfig(browser= "android", device_name = "Google Nexus 7 HD Emulator")

    SAMSUNG_S4 = RunConfig(browser= "android", device_name = "Samsung Galaxy S4 Emulator")

    IPHONE_4S = RunConfig(browser= "iPhone", device_name = "iPhone 4s")

    IPHONE_5 = RunConfig(browser= "iPhone", device_name = "iPhone 5")

    IPHONE_6 = RunConfig(browser= "iPhone", device_name = "iPhone 6")

    IPHONE_6_PLUS = RunConfig(browser= "iPhone", device_name = "iPhone 6 Plus")

    IPAD_AIR  = RunConfig(browser= "iPhone", device_name = "iPad Air")

    IPAD_2  = RunConfig(browser= "iPhone", device_name = "iPad 2")
