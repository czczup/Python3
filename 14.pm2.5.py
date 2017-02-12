#pm2.5
def main():
    PM = eval(input("What is today's PM2.5"))
    if PM > 75:
        print("Unhealthy.Be careful!")
    if PM < 35:
        print("Good.Go running！")
main()
