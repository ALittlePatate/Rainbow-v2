class last :
    def read(self) :
        with open("configs/last/last.txt", "r") as f :
            for line in f :
                last = line

        return last

    def write(self, name) :
        with open("configs/last/last.txt", "a") as f :
            f.seek(0)
            f.truncate()
            f.write(name)
            f.close()