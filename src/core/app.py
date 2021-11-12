import firebase_admin
from firebase_admin import credentials
from ..settings.environments import FB_CLIENT_EMAIL, FB_PRIVATE_KEY, FB_PRIVATE_KEY_ID
import json
import codecs


class App:
    def __init__(self) -> None:
        serviceAccountJSON = self.__getServiceAccountJSON()
        cred = credentials.Certificate(serviceAccountJSON)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)

    def __getServiceAccountJSON(self):
        file = open('serviceAccountKey.json', 'r')
        fileJSON = json.loads(file.read())
        # fileJSON["private_key"] = codecs.decode(
        #     FB_PRIVATE_KEY, "unicode_escape")
        fileJSON["private_key"] = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCZjRTcisgRyKXp\notAMBpj5yEbrr3LkY9YORB+UJ0jd3a8dG8sxPIoNo7OKsuEIHAoBYs8p6ynJ39Pe\ncpOl5CXcxByPYtafKOPMjHO0OYC2F7Qgt0GNkwwa/Ax7MG2gEOW/WFxSUy5s4JrQ\n0yGKDV2Tqwe1JBY3PRjvNRBGFC2xBoac/VYYdW8TTfzq7JJj7pKpcCKybUbWSwL4\n/vaZ5HTCHSfX75UzGQqRXc3ZK+hI8Xk7YzfXZzZ++wBQItJmxr7Uw+4JLPv4XNLr\n+fAUXeaJ66hfF7lQEF1F3frAylAVIWcaTfYlotzO4JPzZFEcLBBZI1/NSlh7V4W6\ny3aHUcXbAgMBAAECggEAGX+4taZkSAkVKEHDISQdVj7V1tYJaHeoeIZZOiNLR0Ya\nNOVvLkDP6ijuVqY9lrj/86/4GA13IJDctbA66E2v+JkmkaxyWKGT3AgnlLJcjKCj\nZzAXdjkI8G2SbbNNQ8tajmvQKlRUPXy6U4WkKFvvghILqHSS2InQW1+T/Bc7aTia\nxIa12mmEIvzOkG1PS2L0JMh769j09BTzfl+FectDnUw8CRa01rBn9NAatwVR4owf\nY3quuWmzmWoUCJC9O2WS1ybwee1kPfPfqzNudV/mpUo/iiiyg4ahYEtcQSosFjsC\nFcoM101b4PHXYZDSCExijSjQuBk+qJT7aD7cm9g4kQKBgQDQ7pt4ht4u3jMsrlhn\ncQDSiKcgYCbuQAR9uABk8dOAM6jEOx8OdN3d+KwwDNb0RHhOSXazCDSB/GLsY39p\n+4o6PbM1NeWle45Ci29J9+JqmvgcuMD+HR4RiL+3p4Sbgo4Lah7ZVHLrNQCk2+JT\n9j4yjtY4zIKHs1JOJ8UCtUNxawKBgQC8JJRsGM42zF8xOvhvcioNxj9suMn7pgCn\nHmZzvHlozrTHORfBHucz/DhkZ3JYy5FwzPvk0oM3+ZsxHs43Q+pICKYyb6nouiCj\noeuS4tj4W/8iZnUrV200HLJT4aiorCR1H/LFK+7BKjY9CTmOgMh5EssQTEbs6hrt\nvU366eJpUQKBgH08ycyxazVE1AAQccVvo0KPzz5E5JEjpo2FYhcgLdtHG/6kQbV0\nsBmCGhSjXaYF9OdYeeJPJMpV8yYnbhSlRvIqUeWvbPyI13lkA02fXQTx54+v319z\nLLbt9Z2suHxPAb4t2lgDmu8KUlx/wWb6z8WWgSqCzCtzff6DMECzTr4JAoGAOck+\ncQkZZUlWP4euQISfGAX4+wqytwEgmDPFIe0UmTVL3xjRC/bS6mugYm5Hd7Bmpm+/\nOmPR+8JFgUvF6MGKVr+ZVEpptFpepgOYmE/mdjnDXix79mju2J+rwgnARLZCqFq8\ntQSuW1P8vrhznio96Ln19raG3kN1K+oF5ngpm1ECgYAStTu3uBMvdFshHumtKRPC\nAm7fvJ+Lf6Lo01kUSEOlrkWs11wpZip3tJf7BYP0/YGHbZ2cOSKc4Qvqctpbn5Og\nVLf3JwwXTWA2cmUJsllvq+I/NJb3ZG1lxtD7zddFwomW3ENfMLyBMgPacmMLyvWu\n1G3Q9rOFly356t946DmKFw==\n-----END PRIVATE KEY-----\n"
        fileJSON["private_key_id"] = FB_PRIVATE_KEY_ID
        fileJSON["client_email"] = FB_CLIENT_EMAIL
        return fileJSON
