from printer import print


from scenes.model import Scene
from scenes.arrival import ArrivalScene


class SlackScene(Scene):
    def run(self):
        print("\nYou grab your phone to message #coreteam to get help.")
        print("Enter your cry for help:")
        value = input()
        print(f"\n[secondary] 8:21 AM - #coreteam: {value}")

        print("[secondary] 8:21 AM - #coreteam: @Jacks - OMG + 😱")
        print("[secondary] 8:21 AM - #coreteam: @Shannon - Do not touch anything")
        print("[secondary] 8:21 AM - #coreteam: @Lauren - I'm not cleaning that up")
        print("[secondary] 8:21 AM - #coreteam: @DanB")
        print(
            "[secondary] 8:21 AM - #coreteam: @Eric - Sorry can't help, with other VCs"
        )
        print(
            "[secondary] 8:21 AM - #coreteam: @Andrew - Please keep Gunner away from the body\n"
        )

        return ArrivalScene()
