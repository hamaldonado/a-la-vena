import caesar

def brute_force(message):
    for i in range(1, 31):
        print (f"key:{i}  Resultado:{caesar.decode(message, i)}")


if __name__ == "__main__":
    msg = "6rmrFCrEBmrFGnmABpurmrAmrymCnEDHrmqrGEnFmqrmyBFmnEoHFGBFk"
    brute_force(msg)