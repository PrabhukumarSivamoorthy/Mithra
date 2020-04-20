from workshop.apiTestFile import APPLICATION

def main():
    try:
        print("Initilizing Mithra...")
        app = APPLICATION()
        app.run()
        
    except Exception, exc:
        print exc
        raise    


if __name__ =="__main__":
    main()
    