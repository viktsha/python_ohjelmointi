jarjestysnumero = int(input("Anna kuukauden numero (1-12):"))

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

vuodenaika = vuodenajat[jarjestysnumero-1]

print(f"{jarjestysnumero}. vuodenaika on {vuodenaika}")