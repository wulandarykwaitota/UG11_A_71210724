def cetakHuruf():
    kata = input('masukkan kata :')
    x = len(kata)
    if x %2 ==0:
        kanan = kata[-3::]
        kiri = kata[0:3]
        print('Huruf yang diambil pada kata', kata, 'adalah',kiri,'dan',kanan)
    
    elif x%2 ==1:
        y = x//2
        kata = (kata[y-1:y+2])
        print('Huruf yang diambil pada kata',kata,'adalah',kata)

cetakHuruf()