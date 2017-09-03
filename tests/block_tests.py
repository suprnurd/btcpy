import unittest
from blockchainlib.ds.block import *
from blockchainlib.ds.parsing import *
from binascii import hexlify, unhexlify

blocks = [{
    'hash': "0000000000000178a6f26995c9937e99d42c1d4d4131ad162e283d34a9633780",
    'raw':
        "00000020751406511dd24f6972987b00049e8ddcaa53e9a5402a9c3e320000000000000061acb5579267e3ebec145871380c3e4f9759fbe1476e76149fed1647980d84522bf92"
            "359a1ca041a55a1eee30c01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff2a03452c11042bf923592f244d696e65642062"
            "792037706f6f6c2e636f6d2f0100000048db000000000000ffffffff0126e65409000000001976a914255c8fce64bc2c994f6f1d2cc85579983601bb5488ac000000000100000"
            "0017363302165009d464cad2867df7f3d97979258ff9cf2c94fe5329ec149992a0a01000000d900473044022043781eaef3d91c3dec2ecc7092dda492d785aad19769e227ba99"
            "343656b32bb1022006ea05e1c7578774e3cd6b77e23ae62c9335bf4108dd17a16ab7857be7fd58700147304402203a7b1e1426099fc37789df566646886a105a2062b5170f916"
            "23fbf03005d6a9502207cce979d47a1ded7a1db101a204048e635c6f1eb7f89bbc08bc7a0ac3c7ddb2d0147522102632178d046673c9729d828cfee388e121f497707f810c131"
            "e0d3fc0fe0bd66d62103a0951ec7d3a9da9de171617026442fcd30f34d66100fab539853b43f508787d452aeffffffff0240420f000000000017a9140c3b53daff6dea5651309"
            "8d72aa18138fdda503287f2dd647e0000000017a9148ce5408cfeaddb7ccb2545ded41ef4781094548487000000000100000001b1caab76a5198100d2daaeb22f5a73786c1be1"
            "dd4979def0844b4af6a2b5759701000000da004730440220679c47ac4cc8135b322483dd4e53979ec650225d8acb3da4f5d8cf7746988d4a02207e96e67bc865632ffd29bf1f9"
            "bd5f51d2a69de94fa8e93ecbfd9dc0fc58fd2ee01483045022100810052ac4d4731433bb8800e767d52933b201223651a2aea5019818c83b47d8d022023cd498fe594cdfc9d5b"
            "0861421731d7a67f0253ab413cae3c2b518eba9176d00147522102632178d046673c9729d828cfee388e121f497707f810c131e0d3fc0fe0bd66d62103a0951ec7d3a9da9de17"
            "1617026442fcd30f34d66100fab539853b43f508787d452aeffffffff0240420f000000000017a9149177db5b7b36c858e779e875398874b44b4291278724f7537e0000000017"
            "a9148ce5408cfeaddb7ccb2545ded41ef4781094548487000000000100000001c79a11e2d9e715cf74509a4fd892065cc5a29e5d47ea955bd473388ae15702fe01000000db004"
            "83045022100d5356c3cbccac67a82d8ae2a9164158c89a9d697bf8d1ab3365f721180a361cf022046dc8e00e755d9600bce5273ab429daf64d94387809708576a4938e0b8121b"
            "df01483045022100d6cb1f5f720a01f05526316e6a52c4b26a936fe09b7ec8f2c449ac1bf4e87c9202205d8cc290a6e7758615ea2df2d8736f49fbe54fe538a8ea169803beed4"
            "5d53c130147522102632178d046673c9729d828cfee388e121f497707f810c131e0d3fc0fe0bd66d62103a0951ec7d3a9da9de171617026442fcd30f34d66100fab539853b43f"
            "508787d452aeffffffff0240420f000000000017a91407f8e7ae1e3a611818b11c571fc1f37e7c9485f3870206387e0000000017a9148ce5408cfeaddb7ccb2545ded41ef4781"
            "094548487000000000100000001b9f2d7513c823afcc6dc0e0afb64d61da468ba0e26da9bd909a4eaa45813fe0a010000006b483045022100c31aaa1fb2cbd5fef776baffa9e2"
            "171903b5826846c2d8decf6d9bd1403a5c2a022074f88e660647006b4f1557198c0f4e3b502cb1e91a2388081280aa6eee81af590121036576eed4dd5de137031c22b1375cd0a"
            "67b9e17a4efd8cab8b07b1fa7e1679791feffffff02459e62060000000017a914c69533b4df0e4afe850863ad19d4775057023d5e87d2ebf89e6f0000001976a914c5b1f3478d"
            "a9559680472a48d8eda4f42d0a3bee88ac3b2c11000100000001c4f627209c6f4bf1851986b543924fde50b40d1a12a93022534fb4d842e51975010000006b483045022100c0b"
            "aa3c2d3eb4cc7ecc7636a2c4ce273bc362a287f9d09f3a4353018c5d4832b02204268cae2e2921a5164663a550c9f965d05e81fc0d77d9ea549913c1cfc778a730121038516ab"
            "e640be18deeab8cbb129c2265a58a5102b2c187c3b00041c4b64bafa38ffffffff0323020000000000001976a9146e9fb388545eeac583779c09e212298249e4a91388acac120"
            "100000000001976a9141e7034e686d3df27a484a8e06e99bc9b2a82a63a88ac0000000000000000026a000000000001000000012ddfbd28c7137c773ca8e88bb9887dfe503c3f"
            "a530c909186803c913631d4f6b010000006b483045022100abaa2211961cf9dd4238e764286638e9d1f8b8e323f9f45729ddd8c4aa505449022041d90fccbb619d87d8edb7fe1"
            "5f5a1117573a186ca7bf2e421087e42cd1a4f7a0121038516abe640be18deeab8cbb129c2265a58a5102b2c187c3b00041c4b64bafa38ffffffff0323020000000000001976a9"
            "146e9fb388545eeac583779c09e212298249e4a91388acac120100000000001976a9141e7034e686d3df27a484a8e06e99bc9b2a82a63a88ac0000000000000000026a0000000"
            "00001000000015e29111ced61eb17fedfbcecce965cccf252a22c40667707c909e9d91f1ae826030000006a473044022034b5aa260e3a8de2da3a4daa99d0deb556d68a6dd627"
            "551a8a768748df9a2b2c022042a12fce0105bd76742457e0a03c2f56397cecb4d0080605952f009788ed549c012103b64e32e5f62e03701428fb1e3151e9a57f149c67708f6164a23"
            "5c8199fe17cc2ffffffff0510270000000000001976a91413b29e222f7e96f7fc4e51778215d2071c25fe2a88ac10270000000000001976a91413b29e222f7e96f7fc4e51778215d2"
            "071c25fe2a88aca0860100000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac5cd9d30c000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060"
            "c88ac0000000000000000026a000000000001000000029d796553688d8222bb83fe004c1afdc378c94ddb9cd9048b6310162ad341f7da020000006a4730440220095b1cd23f1dc234"
            "18062ef38376d6582fc04cda323a8b05ea82dd12cd937f3002200153083fd8da6cb810c04e4444361aaf8318feaa006c198babd82609c397f48e012103b64e32e5f62e03701428fb1"
            "e3151e9a57f149c67708f6164a235c8199fe17cc2ffffffff4d195edfbfb89c1e06eef5fd0ac799c0618917864e9db9f5babff9994694c275030000006b483045022100b8d223a5d4"
            "cb5ad084f398d32264f76252b27aa964b75a78c62dc994697e313502201938f8a83262a47a46d29b5e3d34ca10d99eb2a0b4e823cb20aa0cedd1455367012103b64e32e5f62e03701"
            "428fb1e3151e9a57f149c67708f6164a235c8199fe17cc2ffffffff0510270000000000001976a914464d545207666eae5cf656eb2e3ef3683c3845d088ac10270000000000001976"
            "a914464d545207666eae5cf656eb2e3ef3683c3845d088aca0860100000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac46931604000000001976a91413d35"
            "ad337dd80a055757e5ea0a45b59fee3060c88ac0000000000000000026a0000000000010000000140255d7edf9a8e9896b49883b984450d98b85b685f6480ea64ef3110d1e24ea101"
            "0000006b483045022100dc91cc36ab937a96fca53b60d2e3d7d3e0fe1df1780301de69a90769c51fc311022001546d83d88a951bbefb4dfa4755fead9a1f92a1a89622fa56cf7e466"
            "5a553890121024e68ae959c2e5ea5930d7fb0b0b657237345002a2f796f3cb5c88ef169f7ae1fffffffff026887eb0b000000001976a91483733adf835c38ff1f38f9c94f20304611"
            "80233f88ac0000000000000000516a4c4e424c466f7220676f6f64206c75636b2c2049206c696b65206d79207268796d6573206174726f63696f75730a537570657263616c6166726"
            "167696c697374696365787069616c69646f63696f7573000000000200000001749b7bb91129f6cfdf0e718bb93b69913aa042b5b95d0a75b53ddaf620f47b6b010000006a47304402"
            "20457a6bba7567339990a908aa8e01581bafef6fed897ec38665db6289b08e43c902203daeff344efb8c0ba115e6a438352fbbb18fb8faff908ef537989c0582d78df20121022492b"
            "726a9f9145a55de46c30788e464078e177f6f06517441a0a2e0a983cea6feffffff02d0070000000000001976a9142d7cd96c8c3c5abed84b00f14925fcd850b0996488ac6cd9d508"
            "000000001976a91400e11e0f2b95cf19618a469b04e5ce4c2771269088ac432c11000200000001a10a003534b680f823eb6327f18f7d25b62099c68514cc2a9c21e3e022b89f80010"
            "000006b483045022100a2147a82ffb809ae8c9ca1cb19e0ae47ea59820a96c4f08d1a6a18bd122df45e02205cf7aa73155ef4ea151268a01c4782d1abb067257d4d6eb648fb103cb6"
            "aed2f0012103b3291cab50639641beef486d0ee263ef670528407fb2ba9eb4c313babf3f93d1feffffff02ad9e1708000000001976a914f11e2d2a4d92ce294c587eb8c334cb95c29"
            "0126388acd0070000000000001976a914cf0fe6b32ab653dfab2ecc97b1ab07133ceef3b688ac162c1100"},

    {
        'hash': "00000000000004495fb1df359b689d92525fd56fcc5d32e832a4d85b378aa973",
        'raw':
            "04000000803763a9343d282e16ad31414d1d2cd4997e93c99569f2a678010000000000004af2cfcf85812bc49dfe0c021353ca8bc0f51a6c0c37341cbcb9dbfe69b109d158f92359a1ca041ac282170205010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff2503462c1100045cf9235904ae6e70310c27852359af87235995010100082f5345475749542fffffffff02d04e5009000000001976a914e58e176ed4e0b65af4719de10b28697a1cc8b59188ac0000000000000000266a24aa21a9edfcb8adcad672e717fc5031797f44084164517ec62423bd80c72080e21023005b01200000000000000000000000000000000000000000000000000000000000000000000000000100000001f062a2769ae1bca9c877ad596917c201f9276028d00a8be2ba6caa231f948010000000006b483045022100dcd74566a27e0216820bf1f1c82c8c2cc268003b89b107f5b2eed70e4e6f8f3c02204912e5dc37e0df238685aa25c5af98871edc08999aaccf6087a7b2456ffae8ab0121024e68ae959c2e5ea5930d7fb0b0b657237345002a2f796f3cb5c88ef169f7ae1fffffffff02e073eb0b000000001976a91483733adf835c38ff1f38f9c94f2030461180233f88ac0000000000000000516a4c4e424c466f7220676f6f64206c75636b2c2049206c696b65206d79207268796d6573206174726f63696f75730a537570657263616c6166726167696c697374696365787069616c69646f63696f7573000000000100000001b2da1ead2f96efbb8aa2a2d0f74655fc6396745acdd9989d6c2e1f3c8e510a8b00000000fd660100473044022078e21a2dcba2b35b45cb6ea143a831962c72f205249561f14f9c33bb581168f502203c624845c3a18641b0beee70245a3e38aaa8a4afa01bfebcde7b7a1db73ae74c0147304402207fdb4ee7c9f91b43cc58276c641d4686937655553961e7b559d53a93f46c1b3c02200cfd8c527631310b54fb26f0df0a538803fc4b7aeba3735c03d970d31f56f085014730440220475b25c35a8e15e256f3331988cabd4c8bcc3f2f7d172b4a05da43d6ab0b90e10220799b526aec1ad03b450e30bceab70031f4a4864ff8f76755ecbbdc1acce3daa3014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02900d3e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d01006c870c00000000005fc8fd45e3777fa41f75c0862c10648541074fe3aa70f126a9a3bdd2c4512d46000000000100000001e59d218d60ea0d697f9345d9096f6943d8289cd7c6277e0669f31bfce6e5722600000000fd6801004730440220528a59f989522b05750c719cdcc6ba6e5aa0f0755b4618f01c87b78fbf37ccef0220232108ed677ce5d53e0a8f0c6810fb49576d6fe12dbda41dbfffb8376e0959c001483045022100df08c88458874ff4bca8403883f2674d7e1620200cbeb000702f74823ae9bf18022022d09cc8fe53d516df71ddc0674a6b90b6ffc1cc25d2976c81b5332a7a6b13e001483045022100f786162240a5be1231e7dcfaf6e4c53fab50a6a8e29f772173d0388c35854a1502201ceb4f663ef445ba801f6a28042df29016099f3bad4cff8cc5cc87b804f61281014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02a8093e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d010076870c0000000000f2097f577ac812c33a583d36db7fdb97a751023cb8935cd357f9e451d565a74800000000010000000137f112a6fdbb347e84ba3c0b1a18650bb640cbf4838fd0f3cc95fa0a7060b77d00000000fd67010047304402207ce0c66982709b4d6b6b04d6e59febe86c7101cb313e3ecef2ceb409a0350c0602202e6cf059e619e3bac5f41e7a8e949dbcf6d6ba3b344397546c88209eb5f27b8b01483045022100caa4a03cbdebee28f6ca2095b538f62a455ca2be28d0726c6d2642403fac900202202d8768dadbb827cb4c1bbe2766a7915d4fd24c8c8c6c797358e3f0db10e9f6820147304402204866411ca7970928535fb73f52a7bb19358a63eaeba05d2b85b47bb2fc835ef602207f4db7ecc486e07a9f8d76b43bc5503bfb2d631f77ce5c7a893fdabb24f25cc4014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02c0053e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d010080870c0000000000b0394ec686b9848c685ed0695fca5f29af6b1c681b2904ea71efe262ff189f9700000000"}]
# First non-zero digit changed
f_blocks = [{
    'hash': "0000000000000978a6f26995c9937e99d42c1d4d4131ad162e283d34a9633780",
    'raw':
        "00000090751406511dd24f6972987b00049e8ddcaa53e9a5402a9c3e320000000000000061acb5579267e3ebec145871380c3e4f9759fbe1476e76149fed1647980d84522bf92359a1ca041a55a1eee30c01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff2a03452c11042bf923592f244d696e65642062792037706f6f6c2e636f6d2f0100000048db000000000000ffffffff0126e65409000000001976a914255c8fce64bc2c994f6f1d2cc85579983601bb5488ac0000000001000000017363302165009d464cad2867df7f3d97979258ff9cf2c94fe5329ec149992a0a01000000d900473044022043781eaef3d91c3dec2ecc7092dda492d785aad19769e227ba99343656b32bb1022006ea05e1c7578774e3cd6b77e23ae62c9335bf4108dd17a16ab7857be7fd58700147304402203a7b1e1426099fc37789df566646886a105a2062b5170f91623fbf03005d6a9502207cce979d47a1ded7a1db101a204048e635c6f1eb7f89bbc08bc7a0ac3c7ddb2d0147522102632178d046673c9729d828cfee388e121f497707f810c131e0d3fc0fe0bd66d62103a0951ec7d3a9da9de171617026442fcd30f34d66100fab539853b43f508787d452aeffffffff0240420f000000000017a9140c3b53daff6dea56513098d72aa18138fdda503287f2dd647e0000000017a9148ce5408cfeaddb7ccb2545ded41ef4781094548487000000000100000001b1caab76a5198100d2daaeb22f5a73786c1be1dd4979def0844b4af6a2b5759701000000da004730440220679c47ac4cc8135b322483dd4e53979ec650225d8acb3da4f5d8cf7746988d4a02207e96e67bc865632ffd29bf1f9bd5f51d2a69de94fa8e93ecbfd9dc0fc58fd2ee01483045022100810052ac4d4731433bb8800e767d52933b201223651a2aea5019818c83b47d8d022023cd498fe594cdfc9d5b0861421731d7a67f0253ab413cae3c2b518eba9176d00147522102632178d046673c9729d828cfee388e121f497707f810c131e0d3fc0fe0bd66d62103a0951ec7d3a9da9de171617026442fcd30f34d66100fab539853b43f508787d452aeffffffff0240420f000000000017a9149177db5b7b36c858e779e875398874b44b4291278724f7537e0000000017a9148ce5408cfeaddb7ccb2545ded41ef4781094548487000000000100000001c79a11e2d9e715cf74509a4fd892065cc5a29e5d47ea955bd473388ae15702fe01000000db00483045022100d5356c3cbccac67a82d8ae2a9164158c89a9d697bf8d1ab3365f721180a361cf022046dc8e00e755d9600bce5273ab429daf64d94387809708576a4938e0b8121bdf01483045022100d6cb1f5f720a01f05526316e6a52c4b26a936fe09b7ec8f2c449ac1bf4e87c9202205d8cc290a6e7758615ea2df2d8736f49fbe54fe538a8ea169803beed45d53c130147522102632178d046673c9729d828cfee388e121f497707f810c131e0d3fc0fe0bd66d62103a0951ec7d3a9da9de171617026442fcd30f34d66100fab539853b43f508787d452aeffffffff0240420f000000000017a91407f8e7ae1e3a611818b11c571fc1f37e7c9485f3870206387e0000000017a9148ce5408cfeaddb7ccb2545ded41ef4781094548487000000000100000001b9f2d7513c823afcc6dc0e0afb64d61da468ba0e26da9bd909a4eaa45813fe0a010000006b483045022100c31aaa1fb2cbd5fef776baffa9e2171903b5826846c2d8decf6d9bd1403a5c2a022074f88e660647006b4f1557198c0f4e3b502cb1e91a2388081280aa6eee81af590121036576eed4dd5de137031c22b1375cd0a67b9e17a4efd8cab8b07b1fa7e1679791feffffff02459e62060000000017a914c69533b4df0e4afe850863ad19d4775057023d5e87d2ebf89e6f0000001976a914c5b1f3478da9559680472a48d8eda4f42d0a3bee88ac3b2c11000100000001c4f627209c6f4bf1851986b543924fde50b40d1a12a93022534fb4d842e51975010000006b483045022100c0baa3c2d3eb4cc7ecc7636a2c4ce273bc362a287f9d09f3a4353018c5d4832b02204268cae2e2921a5164663a550c9f965d05e81fc0d77d9ea549913c1cfc778a730121038516abe640be18deeab8cbb129c2265a58a5102b2c187c3b00041c4b64bafa38ffffffff0323020000000000001976a9146e9fb388545eeac583779c09e212298249e4a91388acac120100000000001976a9141e7034e686d3df27a484a8e06e99bc9b2a82a63a88ac0000000000000000026a000000000001000000012ddfbd28c7137c773ca8e88bb9887dfe503c3fa530c909186803c913631d4f6b010000006b483045022100abaa2211961cf9dd4238e764286638e9d1f8b8e323f9f45729ddd8c4aa505449022041d90fccbb619d87d8edb7fe15f5a1117573a186ca7bf2e421087e42cd1a4f7a0121038516abe640be18deeab8cbb129c2265a58a5102b2c187c3b00041c4b64bafa38ffffffff0323020000000000001976a9146e9fb388545eeac583779c09e212298249e4a91388acac120100000000001976a9141e7034e686d3df27a484a8e06e99bc9b2a82a63a88ac0000000000000000026a000000000001000000015e29111ced61eb17fedfbcecce965cccf252a22c40667707c909e9d91f1ae826030000006a473044022034b5aa260e3a8de2da3a4daa99d0deb556d68a6dd627551a8a768748df9a2b2c022042a12fce0105bd76742457e0a03c2f56397cecb4d0080605952f009788ed549c012103b64e32e5f62e03701428fb1e3151e9a57f149c67708f6164a235c8199fe17cc2ffffffff0510270000000000001976a91413b29e222f7e96f7fc4e51778215d2071c25fe2a88ac10270000000000001976a91413b29e222f7e96f7fc4e51778215d2071c25fe2a88aca0860100000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac5cd9d30c000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac0000000000000000026a000000000001000000029d796553688d8222bb83fe004c1afdc378c94ddb9cd9048b6310162ad341f7da020000006a4730440220095b1cd23f1dc23418062ef38376d6582fc04cda323a8b05ea82dd12cd937f3002200153083fd8da6cb810c04e4444361aaf8318feaa006c198babd82609c397f48e012103b64e32e5f62e03701428fb1e3151e9a57f149c67708f6164a235c8199fe17cc2ffffffff4d195edfbfb89c1e06eef5fd0ac799c0618917864e9db9f5babff9994694c275030000006b483045022100b8d223a5d4cb5ad084f398d32264f76252b27aa964b75a78c62dc994697e313502201938f8a83262a47a46d29b5e3d34ca10d99eb2a0b4e823cb20aa0cedd1455367012103b64e32e5f62e03701428fb1e3151e9a57f149c67708f6164a235c8199fe17cc2ffffffff0510270000000000001976a914464d545207666eae5cf656eb2e3ef3683c3845d088ac10270000000000001976a914464d545207666eae5cf656eb2e3ef3683c3845d088aca0860100000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac46931604000000001976a91413d35ad337dd80a055757e5ea0a45b59fee3060c88ac0000000000000000026a0000000000010000000140255d7edf9a8e9896b49883b984450d98b85b685f6480ea64ef3110d1e24ea1010000006b483045022100dc91cc36ab937a96fca53b60d2e3d7d3e0fe1df1780301de69a90769c51fc311022001546d83d88a951bbefb4dfa4755fead9a1f92a1a89622fa56cf7e4665a553890121024e68ae959c2e5ea5930d7fb0b0b657237345002a2f796f3cb5c88ef169f7ae1fffffffff026887eb0b000000001976a91483733adf835c38ff1f38f9c94f2030461180233f88ac0000000000000000516a4c4e424c466f7220676f6f64206c75636b2c2049206c696b65206d79207268796d6573206174726f63696f75730a537570657263616c6166726167696c697374696365787069616c69646f63696f7573000000000200000001749b7bb91129f6cfdf0e718bb93b69913aa042b5b95d0a75b53ddaf620f47b6b010000006a4730440220457a6bba7567339990a908aa8e01581bafef6fed897ec38665db6289b08e43c902203daeff344efb8c0ba115e6a438352fbbb18fb8faff908ef537989c0582d78df20121022492b726a9f9145a55de46c30788e464078e177f6f06517441a0a2e0a983cea6feffffff02d0070000000000001976a9142d7cd96c8c3c5abed84b00f14925fcd850b0996488ac6cd9d508000000001976a91400e11e0f2b95cf19618a469b04e5ce4c2771269088ac432c11000200000001a10a003534b680f823eb6327f18f7d25b62099c68514cc2a9c21e3e022b89f80010000006b483045022100a2147a82ffb809ae8c9ca1cb19e0ae47ea59820a96c4f08d1a6a18bd122df45e02205cf7aa73155ef4ea151268a01c4782d1abb067257d4d6eb648fb103cb6aed2f0012103b3291cab50639641beef486d0ee263ef670528407fb2ba9eb4c313babf3f93d1feffffff02ad9e1708000000001976a914f11e2d2a4d92ce294c587eb8c334cb95c290126388acd0070000000000001976a914cf0fe6b32ab653dfab2ecc97b1ab07133ceef3b688ac162c1100"},
    {
        'hash': "00000000000007495fb1df359b689d92525fd56fcc5d32e832a4d85b378aa973",
        'raw':
            "09000000803763a9343d282e16ad31414d1d2cd4997e93c99569f2a678010000000000004af2cfcf85812bc49dfe0c021353ca8bc0f51a6c0c37341cbcb9dbfe69b109d158f92359a1ca041ac282170205010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff2503462c1100045cf9235904ae6e70310c27852359af87235995010100082f5345475749542fffffffff02d04e5009000000001976a914e58e176ed4e0b65af4719de10b28697a1cc8b59188ac0000000000000000266a24aa21a9edfcb8adcad672e717fc5031797f44084164517ec62423bd80c72080e21023005b01200000000000000000000000000000000000000000000000000000000000000000000000000100000001f062a2769ae1bca9c877ad596917c201f9276028d00a8be2ba6caa231f948010000000006b483045022100dcd74566a27e0216820bf1f1c82c8c2cc268003b89b107f5b2eed70e4e6f8f3c02204912e5dc37e0df238685aa25c5af98871edc08999aaccf6087a7b2456ffae8ab0121024e68ae959c2e5ea5930d7fb0b0b657237345002a2f796f3cb5c88ef169f7ae1fffffffff02e073eb0b000000001976a91483733adf835c38ff1f38f9c94f2030461180233f88ac0000000000000000516a4c4e424c466f7220676f6f64206c75636b2c2049206c696b65206d79207268796d6573206174726f63696f75730a537570657263616c6166726167696c697374696365787069616c69646f63696f7573000000000100000001b2da1ead2f96efbb8aa2a2d0f74655fc6396745acdd9989d6c2e1f3c8e510a8b00000000fd660100473044022078e21a2dcba2b35b45cb6ea143a831962c72f205249561f14f9c33bb581168f502203c624845c3a18641b0beee70245a3e38aaa8a4afa01bfebcde7b7a1db73ae74c0147304402207fdb4ee7c9f91b43cc58276c641d4686937655553961e7b559d53a93f46c1b3c02200cfd8c527631310b54fb26f0df0a538803fc4b7aeba3735c03d970d31f56f085014730440220475b25c35a8e15e256f3331988cabd4c8bcc3f2f7d172b4a05da43d6ab0b90e10220799b526aec1ad03b450e30bceab70031f4a4864ff8f76755ecbbdc1acce3daa3014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02900d3e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d01006c870c00000000005fc8fd45e3777fa41f75c0862c10648541074fe3aa70f126a9a3bdd2c4512d46000000000100000001e59d218d60ea0d697f9345d9096f6943d8289cd7c6277e0669f31bfce6e5722600000000fd6801004730440220528a59f989522b05750c719cdcc6ba6e5aa0f0755b4618f01c87b78fbf37ccef0220232108ed677ce5d53e0a8f0c6810fb49576d6fe12dbda41dbfffb8376e0959c001483045022100df08c88458874ff4bca8403883f2674d7e1620200cbeb000702f74823ae9bf18022022d09cc8fe53d516df71ddc0674a6b90b6ffc1cc25d2976c81b5332a7a6b13e001483045022100f786162240a5be1231e7dcfaf6e4c53fab50a6a8e29f772173d0388c35854a1502201ceb4f663ef445ba801f6a28042df29016099f3bad4cff8cc5cc87b804f61281014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02a8093e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d010076870c0000000000f2097f577ac812c33a583d36db7fdb97a751023cb8935cd357f9e451d565a74800000000010000000137f112a6fdbb347e84ba3c0b1a18650bb640cbf4838fd0f3cc95fa0a7060b77d00000000fd67010047304402207ce0c66982709b4d6b6b04d6e59febe86c7101cb313e3ecef2ceb409a0350c0602202e6cf059e619e3bac5f41e7a8e949dbcf6d6ba3b344397546c88209eb5f27b8b01483045022100caa4a03cbdebee28f6ca2095b538f62a455ca2be28d0726c6d2642403fac900202202d8768dadbb827cb4c1bbe2766a7915d4fd24c8c8c6c797358e3f0db10e9f6820147304402204866411ca7970928535fb73f52a7bb19358a63eaeba05d2b85b47bb2fc835ef602207f4db7ecc486e07a9f8d76b43bc5503bfb2d631f77ce5c7a893fdabb24f25cc4014c8b532102bcdbcb324179b7648e2c7802da2c1a49ae94b51188d86e7352b39257f6bba56c2102fe22fdac89648502a6eeefd84b1616142e267efb1f54fa0932380ae2a14e764421031f1f73c3723efda2a31298729e56f69acfe0751c6520f69ff6f0941998634c462102fddf017fa0899ae0ea23cbd7f9b159b9d9fa8f56c62d55706913e407bb49125654aeffffffff02c0053e060000000017a914716370a50fa600b4ecc34312b9d0d5f3c294166b870000000000000000326a3045584f4e554d010080870c0000000000b0394ec686b9848c685ed0695fca5f29af6b1c681b2904ea71efe262ff189f9700000000"}]
# Shorter dummy blocks
dummy_blocks = [{
    'hash': "0001426804",
    'raw': "00014268046f63696ff7573006ad31414d1d2cd4997e93c99569f0"}]


class TestBlock(unittest.TestCase):
    def test_block_deserialize_serialize(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(blocks[i]['raw'])
            serial_block = unhex_block.serialize()
            self.assertEqual(blocks[i]['raw'], hexlify(serial_block).decode())

    def test_block_hash(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(blocks[i]['raw'])
            self.assertEqual(blocks[i]['hash'], unhex_block.hash())

    def test_block_header(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(blocks[i]['raw'])
            unhex_header = BlockHeader.unhexlify(blocks[i]['raw'])
            self.assertEqual(hexlify(unhex_block.header.serialize()), hexlify(unhex_header.serialize()))

    def test_fail_block_deserialize_serialize(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(f_blocks[i]['raw'])
            serial_block = unhex_block.serialize()
            self.assertNotEqual(blocks[i]['raw'], hexlify(serial_block).decode())

    def test_fail_block_hash(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(f_blocks[i]['raw'])
            self.assertNotEqual(blocks[i]['hash'], unhex_block.hash())

    def test_fail_block_header(self):
        for i in range(len(blocks)):
            unhex_block = Block.unhexlify(blocks[i]['raw'])
            unhex_header = BlockHeader.unhexlify(f_blocks[i]['raw'])
            self.assertNotEqual(hexlify(unhex_block.header.serialize()), hexlify(unhex_header.serialize()))

    def test_stop_iteration(self):
        for i in range(len(dummy_blocks)):
            with self.assertRaises(StopIteration):
                Block.unhexlify(dummy_blocks[i]['raw'])
            with self.assertRaises(StopIteration):
                Block.unhexlify(dummy_blocks[i]['raw']).serialize()

    def test_empty_deserialized_string(self):
        for i in range(len(blocks)):
            parser = BlockParser(bytearray(unhexlify(blocks[i]['raw'])))
            parser.get_block_header()
            parser.get_txns()
            with self.assertRaises(StopIteration):
                parser >> 1

    def test_incomplete_parsing_exception(self):
        for i in range(len(blocks)):
            aug_raw = blocks[i]['raw'] + "ff"
            with self.assertRaises(IncompleteParsingException):
                Block.unhexlify(aug_raw)


if __name__ == '__main__':
    unittest.main()