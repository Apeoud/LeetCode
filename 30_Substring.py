class Solution(object):
    @staticmethod
    def get_index(s, word):
        res = []
        for i in range(len(s) - len(word) + 1):
            if s[i:i + len(word)] == word:
                res.append(i)
        return res

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = sum([len(e) for e in words])
        res = []
        index = []

        # 第一步获取index
        for word in words:
            index.append(self.get_index(s, word))
        for ind in index:
            if len(ind) < 1:
                return []
        # 构建word和index 的dict
        word_index = dict()

        for i, ind in enumerate(index):
            for j in ind:
                if j in word_index.keys():
                    if words[i] not in word_index[j]:
                        word_index[j].append(words[i])
                else:
                    word_index.setdefault(j, [words[i]])

        print(word_index)
        # 第二步 遍历寻找

        for i in range(len(s) - length + 1):
            if i not in word_index.keys():
                continue
            words_set = [e for e in words]
            flag = 0
            path_length = 0
            forward = []
            path = []
            forward.append(word_index[i])
            while True:
                if len(path) == len(words):
                    res.append(i)
                    break
                if sum([len(e) for e in forward]) <= 0:
                    break

                if len(forward[flag]) > 0:
                    path.append(forward[flag][0])
                    path_length += len(forward[flag][0])
                    forward[flag][0:] = forward[flag][1:]
                    flag += 1
                    words_set.remove(path[-1])
                    if i + path_length in word_index.keys():
                        forward.append([e for e in word_index[i + path_length] if e in words_set])
                    else:
                        forward.append([])
                else:
                    forward[0:] = forward[:-1]
                    flag -= 1
                    if len(path) > 0:
                        path_length -= len(path[-1])
                        words_set.append(path[-1])
                        del path[-1]

        print([key for key,value in word_index.items() if len(value) > 1])
        return res


if __name__ == "__main__":
    s = "ttqupktjvqeeylzkyirjnnjuhyrmrhwkaoepyzavshbquaasltdyimtpmmddtzotnsknsnkkumcooeizxmyfyrwlfbqyaetpzdetsodmahcpllqizopzhnmmodkqhdfijjbbxgqansryfhiewzgfmsscvcsfizntkpukvkkjfbjmkutitzoirgmpkfuughnrykbuwnfbqqqckjlgizqbhcqtjkosudlunookbvntodvymggwhyaodqkodygzbrtpfkbifodtszughcdpdffgvpwapdzrwtiefjomxsirrcyygdpjixrfmogctfvpafvfqksncchtgftmklysipxudfyynvoncjvsvpixrpsxumlexjyfbxbgdcfqzvfcgcuctczmtsjngxtdgtkjrnqwrxorsvvyaratwcgpurfaoyfxurgneylyvzrpwmowdqqzsyropwqewvbqojfvkqtfrkxowlmbdcdycumssdwoazhpkmkufdcwpzmnmzopdtngpcyhfwyfxhuhvecajexyfjlrkcioxywnauwfsumpbhwxnazzgwzlincurnioleblaysssejwngvdgucntdadqdxhqgwdmxonxghsmrqazldhfhuakvdbabksjgvvglkdtuxhlnhkymtgtogglmhnnrhwaetgrelkyjrlwbxxnqfjgnptzygmrpkrtezkklwiwqvursrgkyrrmgklgtaykmpgqpsacpkyhfsazmgkkadygnmnioltaczrtrtvigvpnqrncazoacpirbvapivpnwigpeeykzpxphmtjlkjnzrhaphrxeimartpxxphyheoqtjzetiuszbuokloowaqnvhkuzttgzjwssxxmftggubxeoluknkzjtldsgyygjwyctxqaqwhmzeqqrmcewepsrvkyvjgfhehbezbwxkjxqbphoromxfepappwavdhzkkflociynhpowycqmrnsveumtsmovwqhgxsuzdvmkkdjihzxyoruvlioevfbtvjzsdwugritblcltdkrtbnonydtvkwofhnzljvtceodrqrktbendtdstinosjczrsbedwzgcolugcgagmpliudbdqqvbuxumyyquawxqhtwmzwsondwiizlapibmfyyfyoaymzouulivjajzfhhnhunyeqkmojrnztnmuciopqkyqtxxbgkkczihrttiemxdgkpaoxpdnzefudcxkohmpsvjlqrpdoujykjpjaszbygycjvozfarxyakorbrhvchhowtorsqpyotjlhlskcricbwveqecsllgiexbwpsxfmgqttldvcnzgmwkcaowmafwecxdrpcwdkoxezczeqbkexwiyleknlgtnfwgwaealtzpuboytrkxphfnumxhxfanmztizykktjbpnsqgjagyhnldzkkzpnmdohmpfwcaidqvvidhilfszrvadibvxnynvkccjgftmxqhftqnhwfgpdislmnkzmxwybbjigcudsdkouxvqfdhinzvzphbdezdfanpirjnmnxcjxxbccimpjjraqsdwrhbuwtencsbrrdaocdqenewxnpzfhdbamfwkybxatbumewbjatnnylmlamrjrumfzkpxloagputwqufsnuiliwzkkswbmiimszlgolmfhhdabisrfcenzfzjxvnmfxayxlgnzssgayidibwnfbceicqizfufcwfzjlmidhrffzlpchdikhotlgbllxsotxncicnnletsdehinmsyugthnuuyrmomjeoridfthannguvvhntdvomkkhjbtzpfdgyljfgrftgnqbjzqecltqwdxhhtgwymcyzoegfjblxrogqekurflpjkwqdfodttcuhgamrezqxpyovlkoqvezgcrljgpcztxizzwsfvjdmhthsdvlbbmjeeunmjsnervdsryyohbaqwjlzgwaiijmogbcrtpwmmbffzdtggvzcgkbngexqplfvmhpizlulmztmeoukmtmsdohlugclrjhgsyorjkfvmajqogbazntfdcsxjwlcfuiasytbjayvaklpqmprckwfppfynqctklvcjofupfpppbgfpwzrivzxmexawavglqkwgprxwgnmjttbrssaqrxexvetvbbitleacvxzcmnnigozbjzrazvauctrdxzzkdbnzyodndqvjhwmqydsxbstdokilljvqkkrjauydntpwpbmnhemixfnnrxyehtvrgmcgjamyvbulegalkpvjwiwqiwupsrgyglgplsphtjuarwldnhnkrlcziwqcqzawkinvbcewnawezkhmtwwkkamuxcwpbylngylhcpgpsevrocfhbeuleghbkdsobdbjdmrhezwydtrswwbzavkfdriqwbezehikwbrcaqagjrahnbgozsvelduheaglipveqogteizobzxoceebwbgifcrjdyunprrhgzamjzckaaadehgciomnrgzwevjvnccvbdhkekufkwkqdqumhhzynawtwfojhsgkxnucxqjhotzsluesdfsqgolcvbncttmriivgagppbphmjnhmsbeyqrclsrqnkcgvnbbnhqeihlxsygethktxbwlvnbjafpvstyicqmnyykqyqxrxhlxljigylpaqhxlavtemfrkfbcgtzzthmqsvaywlqwdxuozpjddrvpwysesrelasduqdvmqlivkemjwvozmjrlijrcavpdquxgxsspdckphyyfungiyxvignkjkboavlgugalldybmwzrsozbnxyvfniqyleahsjdyjpjmnkyjmrcarfpqfnxtvotgutpmetmoiwcxidgwwkxnpofvbdqwtjfnewcjpozzmbwxgftdpsshhaciduhwdmljinuaetbqxanffjiubddidfrgbyeemrqwfkyjeabdcrihatdbwhmzodhqdnwpemljzmudmyiqpqxpjcsflegajnsmaqdhfrsednjrlrhchgttinaushwdwqszgvgnmyrrnaiyrrcbxvwgjwcdfagcqybywjmkhfcvgkvzcacbvyjgxljcnsefqheoqszaxbvfnshrsjtqkcwhqgjdaqjsxphojgoihlowfxoyihqslmbbunhudqnahuqqcgylrohxlxxweposbstyfasishkbdbrfhsqbiaauxzqeogwrarpfuipmpaovdhambtnkvpguoyyeewwhqlmkvcyneoihyivzdjjyarvppttwsrdidpuytslzhtiheegjpskpjfgzacxstacwrwxnrkmagvhkzpvohffrkmslopfhpigigfvzpibvdiheadshixavlsgzhljyvrhewcflmhhprotrtnzcnbxyufadsjcqalwynbjaksrcjnvccwgrydssksvddztfkrdasocdhthqiculzbezgwrroowtoraaifaaucfdymvirpvsqarzwiqnymiodjpnorniwvnuhieayasqajpythnstwgyfxnvpdglythhclicnaspmkofrbxnxgnefbaueghcbqldetfrwahikxnbanqyveeafgxloepqxatbwbssbbcnapobehzzlfcsmzdadsqaumdqnykozmbaerbiackljmfvnkyseotzcyrpwcfyoiyscbdcfpqodxmqikioadndchsyjawziwsmzxpemhvrehhmrpdrtsuxzpxiruizscmubdapkvgoendvegpzylwacuitqstkwhexmfmwcumhjpeoxtnyfmyjgidwdygzfnzrunpwibfrtkhsfvqkjowpzzncxvbeiaxcombypgriszdywtkfkgujfjnceqgnrfrhruhjbyttxwrtqcaciunqdaskqbxjgqsalzjoyehxbbttftvpqifviafadeklxclicwwcbfbeiuxpquficmdmolmtryfobswfrujsckykhvaxphftvkfkvtdnskbvdaauujowvmjcjlzasgtnrazmvfbnrfkufkqbvgarsjtduvdobyduyfhumkjdpuawgqycxavrjqxflavpzyjzdsvpffvubvrhlrjkrgecxbjkdebcenekfzbmgwhhrapdtanmhrqguzqyfuclhgvoixbotkylmpqfrftyzjgtkzrrtwcacaqmxrdsbbfnsxujdnkeyqziptzkpemtedgdulxyofngciphxznwqnghiisxoessjaxelwczdrfgzvpzufxmsdwclozzurtesskdrofufkchhuiezfqtimvwcuxzntfhlrnefszmebvmvdsuiiprxkpbemcufhbtaozfiyuncpbxttubdjuawlecygwfqaaqqayzasmchpcciygljcofosioagvqgyjxyhwabkdkzhnjfvuqxiwlcgzdmvvvtgutpstqcybdfqomliditbuvhvavqyslemeueamiapngfbuskzbfaxcjudhldzyjmfdqfsbfhonpqihchkhkjjteoarrapbouggbahhiwuzoegsotzycktizwzswrvmlesneawoysnozwgnpfntrgescdnawimiohxvhtlhnzvmxdzokohbxnubrhcnrqxizwdiropfpmrmptazhkdexxiqgkgzcfjccmmtdcysqshgljhutkbtjjjrvrtzxcdbpquuuvmknvsafawymztykfphwihvnmwectywomjdibfnddnsfhqpohxkseifqgjvzhtpvcudgbslhgdmptbdbyptezaxgjshsnxnqtryvjjcrnoiirnlqdewcgvkppshdpvvkotfzcjrrzbarpljushwydjosbxvsuqcijkiovbfvcfottznlgmljvbcwzxqvouezeopcpvxtcnnvmaisoucjvehwdxstsyvymkadfzwiolfaoovcixofdvcivwcpuxpghqjprhzgteihsdlcczifvmosisjerymaqvpieoqxtygncsqeramomcgwupanqmngjfontgnoftejlunfuzvidceztgmlucsfhiscphrwbvforsvnurvzvzzohlabnugucaztiqpjnuzgpvtlmokhpjxwvzxkvfhyfgrnyjyndatsvodjcqstzrpwtohotqmaygqwpoluqgnluswyiqtkiigbwpprhetfmjddaqxqwmeshasrrlbbvietzvkhbeonpsqpioghckzjmubfhcgdmmwoijxjplxedpuofavimwtasugazodnbbblkyuzktepjafqccyqbsqtoyvnnadqcebmfvorruiawoqyqrotlgnbfirujuknynbfkrwblhdhvuhnnxhaewbjgsdrmpencismzrqlytuvnekcbtcfreqywtrjiwymeqbfjrqhknearpcukfaclsahmrswpqlvjmbsdtcnigpzxsukzwmkootchmbxeounavgfrkuzqkbqexadvmnlciojurgbfdohaworgirzsupwrrbmfqxhznqvgzwncnucjiuqtnpnhgmyxnmcejjdzbafaxtckpftazltocgvisvhihjmsurrwrxwqqzahgwhhjcvmlswdnelwnzokqggkdeavfdelbmsmopabhxfwbssquhcmpkwupzpuetihhctysuzzrgwubqmvxpjoziiohxlntvucxpcpjcrckpynflifautbccqjbdywasbxhdpthixuxwhehqljkfkojcxmhvlhpmhwryrzgptflajusvfecpsnurbdomldaucsstrykmdvmorhlwnpogcizelosyrtuvlmrembqrxeiqntnbjbjnlitywmxqhrlugeyugqmfwuvkpinylwowghvdvuveniyvnyqtocylytxnekopicoolltjfonuzmqmkghbkhoialvgxlyhpmvdxpmefzyenosawzbggrojcmrbzpipddscueicfhivxbvwcyclprutfnuedevijnngtvibeqwcttyytcjivfdaszhxdcimqvsjqakvtizobxmubxexchxvgeulhcyzxqkotxjofkejjrfkokhttfoclknunntkggazdlpkvttemzpdlwwgdmirwyljlhwrpwssihcddykrzzukxssdgbwdbjomqmghjyztiewnciedhbphvhmckihlrxykkgrvetooxmbbvieejtleaxinhryzpylzecwlvkzuwdvrlbwuwjaxjlmqckrrjcspfoacaaxxduqqwmksymrhxdzcortztooaepffrccwwsmuhynfkgokknmaghbcvpcagjfzljvkdjgkhvrucfgovsqbbrdxii"
    sub = ["wxnazzgwzlincurnioleblays","txwrtqcaciunqdaskqbxjgqsa","vdhzkkflociynhpowycqmrnsv","sondwiizlapibmfyyfyoaymzo","advmnlciojurgbfdohaworgir","gbwpprhetfmjddaqxqwmeshas","vmjcjlzasgtnrazmvfbnrfkuf","zjxvnmfxayxlgnzssgayidibw","xmsdwclozzurtesskdrofufkc","gglmhnnrhwaetgrelkyjrlwbx","galldybmwzrsozbnxyvfniqyl","ofrbxnxgnefbaueghcbqldetf","ltaczrtrtvigvpnqrncazoacp","psacpkyhfsazmgkkadygnmnio","mztmeoukmtmsdohlugclrjhgs","gjdaqjsxphojgoihlowfxoyih","gpcztxizzwsfvjdmhthsdvlbb","bksjgvvglkdtuxhlnhkymtgto","mewbjatnnylmlamrjrumfzkpx","orsqpyotjlhlskcricbwveqec","wsrdidpuytslzhtiheegjpskp","zehikwbrcaqagjrahnbgozsve","lzjoyehxbbttftvpqifviafad","phyyfungiyxvignkjkboavlgu","zdadsqaumdqnykozmbaerbiac","zxyoruvlioevfbtvjzsdwugri","xtvotgutpmetmoiwcxidgwwkx","cpvxtcnnvmaisoucjvehwdxst","jfgzacxstacwrwxnrkmagvhkz","nubrhcnrqxizwdiropfpmrmpt","rwahikxnbanqyveeafgxloepq","zncxvbeiaxcombypgriszdywt","ottznlgmljvbcwzxqvouezeop","rqguzqyfuclhgvoixbotkylmp","zdsvpffvubvrhlrjkrgecxbjk","kqbvgarsjtduvdobyduyfhumk","azhkdexxiqgkgzcfjccmmtdcy","igcudsdkouxvqfdhinzvzphbd","igylpaqhxlavtemfrkfbcgtzz","ezdfanpirjnmnxcjxxbccimpj","hwydjosbxvsuqcijkiovbfvcf","lzgwaiijmogbcrtpwmmbffzdt","fsqgolcvbncttmriivgagppbp","hsqbiaauxzqeogwrarpfuipmp","mxonxghsmrqazldhfhuakvdba","legajnsmaqdhfrsednjrlrhch","eebwbgifcrjdyunprrhgzamjz","suxzpxiruizscmubdapkvgoen","uvnekcbtcfreqywtrjiwymeqb","pquuuvmknvsafawymztykfphw","bhxfwbssquhcmpkwupzpuetih","pshdpvvkotfzcjrrzbarpljus","edgdulxyofngciphxznwqnghi","pwzrivzxmexawavglqkwgprxw","wimiohxvhtlhnzvmxdzokohbx","sjcqalwynbjaksrcjnvccwgry","qwfkyjeabdcrihatdbwhmzodh","thmqsvaywlqwdxuozpjddrvpw","jdpuawgqycxavrjqxflavpzyj","xphftvkfkvtdnskbvdaauujow","mwkcaowmafwecxdrpcwdkoxez","rrlbbvietzvkhbeonpsqpiogh","gyglgplsphtjuarwldnhnkrlc","sqshgljhutkbtjjjrvrtzxcdb","ihvnmwectywomjdibfnddnsfh","dymvirpvsqarzwiqnymiodjpn","evrocfhbeuleghbkdsobdbjdm","sbbfnsxujdnkeyqziptzkpemt","gmlucsfhiscphrwbvforsvnur","nfbceicqizfufcwfzjlmidhrf","tbqxanffjiubddidfrgbyeemr","fszmebvmvdsuiiprxkpbemcuf","ziwqcqzawkinvbcewnawezkhm","dmolmtryfobswfrujsckykhva","ewcflmhhprotrtnzcnbxyufad","qcebmfvorruiawoqyqrotlgnb","qdnwpemljzmudmyiqpqxpjcsf","xhaewbjgsdrmpencismzrqlyt","iyrrcbxvwgjwcdfagcqybywjm","rhezwydtrswwbzavkfdriqwbe","kljmfvnkyseotzcyrpwcfyoiy","xtygncsqeramomcgwupanqmng","uzoegsotzycktizwzswrvmles","fzlpchdikhotlgbllxsotxnci","rrwrxwqqzahgwhhjcvmlswdne","xtckpftazltocgvisvhihjmsu","aovdhambtnkvpguoyyeewwhql","qenewxnpzfhdbamfwkybxatbu","wqvursrgkyrrmgklgtaykmpgq","ezbwxkjxqbphoromxfepappwa","mzeqqrmcewepsrvkyvjgfhehb","ulzbezgwrroowtoraaifaaucf","rdxzzkdbnzyodndqvjhwmqyds","qtryvjjcrnoiirnlqdewcgvkp","slemeueamiapngfbuskzbfaxc","ssejwngvdgucntdadqdxhqgwd","lhgdmptbdbyptezaxgjshsnxn","qheoqszaxbvfnshrsjtqkcwhq","twwkkamuxcwpbylngylhcpgps","fszrvadibvxnynvkccjgftmxq","hftqnhwfgpdislmnkzmxwybbj","iimszlgolmfhhdabisrfcenzf","mztizykktjbpnsqgjagyhnldz","eacvxzcmnnigozbjzrazvauct","hkhkjjteoarrapbouggbahhiw","uknkzjtldsgyygjwyctxqaqwh","lduheaglipveqogteizobzxoc","ggvzcgkbngexqplfvmhpizlul","omjeoridfthannguvvhntdvom","uulivjajzfhhnhunyeqkmojrn","npofvbdqwtjfnewcjpozzmbwx","altzpuboytrkxphfnumxhxfan","scbdcfpqodxmqikioadndchsy","jfontgnoftejlunfuzvidcezt","pvohffrkmslopfhpigigfvzpi","kkhjbtzpfdgyljfgrftgnqbjz","sllgiexbwpsxfmgqttldvcnzg","exyfjlrkcioxywnauwfsumpbh","hkuzttgzjwssxxmftggubxeol","gftdpsshhaciduhwdmljinuae","uzktepjafqccyqbsqtoyvnnad","fnzrunpwibfrtkhsfvqkjowpz","gpvtlmokhpjxwvzxkvfhyfgrn","hgamrezqxpyovlkoqvezgcrlj","qslmbbunhudqnahuqqcgylroh","otchmbxeounavgfrkuzqkbqex","lcczifvmosisjerymaqvpieoq","ljvtceodrqrktbendtdstinos","jlkjnzrhaphrxeimartpxxphy","judhldzyjmfdqfsbfhonpqihc","lxrogqekurflpjkwqdfodttcu","firujuknynbfkrwblhdhvuhnn","cnnletsdehinmsyugthnuuyrm","stqcybdfqomliditbuvhvavqy","ckzjmubfhcgdmmwoijxjplxed","ttiemxdgkpaoxpdnzefudcxko","jiuqtnpnhgmyxnmcejjdzbafa","eumtsmovwqhgxsuzdvmkkdjih","irbvapivpnwigpeeykzpxphmt","czeqbkexwiyleknlgtnfwgwae","eklxclicwwcbfbeiuxpquficm","xatbwbssbbcnapobehzzlfcsm","ztnmuciopqkyqtxxbgkkczihr","heoqtjzetiuszbuokloowaqnv","vbdhkekufkwkqdqumhhzynawt","fjrqhknearpcukfaclsahmrsw","xlxxweposbstyfasishkbdbrf","qfrftyzjgtkzrrtwcacaqmxrd","ljcofosioagvqgyjxyhwabkdk","ecygwfqaaqqayzasmchpcciyg","lwnzokqggkdeavfdelbmsmopa","vzvzzohlabnugucaztiqpjnuz","hmpsvjlqrpdoujykjpjaszbyg","qecltqwdxhhtgwymcyzoegfjb","kkzpnmdohmpfwcaidqvvidhil","yorjkfvmajqogbazntfdcsxjw","ozmjrlijrcavpdquxgxsspdck","pbmnhemixfnnrxyehtvrgmcgj","hmjnhmsbeyqrclsrqnkcgvnbb","gnmjttbrssaqrxexvetvbbitl","mjeeunmjsnervdsryyohbaqwj","dbdqqvbuxumyyquawxqhtwmzw","pqlvjmbsdtcnigpzxsukzwmko","khfcvgkvzcacbvyjgxljcnsef","gttinaushwdwqszgvgnmyrrna","jawziwsmzxpemhvrehhmrpdrt","jraqsdwrhbuwtencsbrrdaocd","wcumhjpeoxtnyfmyjgidwdygz","zsupwrrbmfqxhznqvgzwncnuc","isxoessjaxelwczdrfgzvpzuf","mkvcyneoihyivzdjjyarvpptt","tblcltdkrtbnonydtvkwofhnz","bvdiheadshixavlsgzhljyvrh","wgyfxnvpdglythhclicnaspmk","jczrsbedwzgcolugcgagmpliu","hbtaozfiyuncpbxttubdjuawl","ysesrelasduqdvmqlivkemjwv","dvegpzylwacuitqstkwhexmfm","qpohxkseifqgjvzhtpvcudgbs","xnqfjgnptzygmrpkrtezkklwi","loagputwqufsnuiliwzkkswbm","qmaygqwpoluqgnluswyiqtkii","kfkgujfjnceqgnrfrhruhjbyt","hhuiezfqtimvwcuxzntfhlrne","fppfynqctklvcjofupfpppbgf","zhnjfvuqxiwlcgzdmvvvtgutp","wfojhsgkxnucxqjhotzsluesd","debcenekfzbmgwhhrapdtanmh","yjyndatsvodjcqstzrpwtohot","eahsjdyjpjmnkyjmrcarfpqfn","neawoysnozwgnpfntrgescdna","amyvbulegalkpvjwiwqiwupsr","orniwvnuhieayasqajpythnst","ckaaadehgciomnrgzwevjvncc","syvymkadfzwiolfaoovcixofd","dssksvddztfkrdasocdhthqic","vcivwcpuxpghqjprhzgteihsd","lcfuiasytbjayvaklpqmprckw","ycjvozfarxyakorbrhvchhowt","fpvstyicqmnyykqyqxrxhlxlj","puofavimwtasugazodnbbblky","nhqeihlxsygethktxbwlvnbja","xbstdokilljvqkkrjauydntpw"]
    print(Solution().findSubstring(s, sub))
