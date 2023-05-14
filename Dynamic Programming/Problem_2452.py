"""
You are given two string arrays, queries and dictionary.

All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter.

Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits.

Return the words in the same order they appear in queries.

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

Constraints:

1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100
All queries[i] and dictionary[j] are composed of lowercase English letters.

"""
from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Edit Distance 그대로 쓰면 Time Exceed.
        def edit_distance(word1, word2):

            cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

            for j in range(len(word2) + 1):
                cache[len(word1)][j] = len(word2) - j
            for i in range(len(word1) + 1):
                cache[i][len(word2)] = len(word1) - i

            for i in range(len(word1) - 1, -1, -1):
                for j in range(len(word2) - 1, -1, -1):
                    if word1[i] == word2[j]:

                        cache[i][j] = cache[i + 1][j + 1]
                    else:
                        cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
            return cache[0][0]

        results = []

        while queries:
            q = queries.pop(0)
            for d in dictionary:
                if edit_distance(q, d) <= 2:
                    results.append(q)
                    break

        return results


solver = Solution()
print(solver.twoEditWords(["word", "note","ants","wood"], ["wood","joke","moat"]))
print(solver.twoEditWords(queries =
["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"],
dictionary =
["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]))
print(solver.twoEditWords(["ircduzbnkalhrrqhgghectjyhtwkbrvasajigogcbcoouinoep",
                           "yglzexzciybnrokzogifsrcchxfwdchlzcnfcauyalqgrtpeuc","svmluxnykpojrybcgocthyennpwwefdduocpzijtyhdpnpzttu","cqyhkcexhviwnlmygjyzcbllesihkgutysoetiebsbnhrrkxtz","pylpigvhsexvhjuwvvrvzcnaiasadqknphnfpahwculffowbjt","pqpcxayffkmthdgjsggcithybjqvzyukfuftrnqzbleeahvaeg","frqahfkzqyuapowviknpswmaxyctbtbcsrbaxglxkxyyqlvddo","szzntzmkdakjmmrhjihdmotknjqhtmlqpcvbboxujiydeqydyk","mjosdfmwwrwegbufwektfigzlmutsnoosblwouvozsmdifbebz","juyifbniaxwheqrbklorxxwqmwiszfchpzwfcyahtogpkxhfly","ivkqkauqrubbuwefklvbllzhkclfcxdkyoudczjrqbisbfkhrh","zptgucodmvckrjdrlqxhepiekycnakqofqbnuhppdqgesfabpl","ueyoqongufysasqfuhsqyjwdkfuvrbrclyhbvevuixoarrlcry","ygacedpcyiolyeoltswsedcpllopnpxsnticbtxynolxdimkqn","boavobzxthjqhswrvlaqeusfhxpxbtotrfhkkhrxleyhsnqcah","ragbcocgmprngufxdefsqxolyljmzoasqrjyprykgblnwrshhw","zjhftehpokrvjwqhmifoqufvhkczmfqigfeakorxhlcdbqmywq","gdplrygityawdnbfvcakidwwmjflzbflqananfycrzvvzpsoul","nitwpyivxagoabmgvnwwswaxiqdozgsocmbfnkfybfyotxeeyf","zavbrdrlswzrwhdboajmodsyjplrnidjevrhmhocylrmnwnavn","ircduzbnkalhrrqrgghectjyhtwkbrvasajigogzbcoouinoep","jiimtpiltaazkqfryuhsugkefvcshjqmcuoeglupvsqhnhclra","vzbstfswityijotcszxqvulyneaptcozxqxohdrsdredoyvczw","ecsyscamxcfjtloukbcilkeajifhubvsdackqypffxcaawjock","xyhdloezbmllzdwdupoevnptcilnjvujguidivytqghqpufknd","xzpibujfouyjgmpojmkornixzcxkzkarewxljuuiqbctnuvxna","mhqihhjbccrrnqsyfjtnncfjsdjhxfawwggfsdhwpterudsbxu","nkwoubzgmvpqlikbjjusnvristkpclflfwbereurtojrmqazez","rtcaxohyebsnifmzrubeysfssyqdpxsbfjyjxzzitpgclozhcd","ddsrjjzzgnttchwoevrhveprhzvfkyiiwnxvcslubduohuzfye","hbidskugbnvpjrjhtdalregqulzovytzuurwtzckjfxlzxawjr","vcqxolgrmortxthtxpcrfrslpxivuausemephayzktfjggznvf","sdwngvzrlxunctjtmehzyeamjdqzxmsxvipkvvqyxehzpzjlrv","idceltsgkfasypzzlyetuffaxnjofabdqwhgwhrezedjsrofwo","pnmfffuxubxrkrsopuizaezgzsfiemlkawbkhdqabnuqapizri","rfroppsvyydqmiqrvrpclmdgqqgkmtazhdicmfgyylsvvetjah","xddnxvsgjlnhqgrivaldbeouzjpwepujhdcjensvjgfhvxtbbw","erztbvnjgnekygjxyuktbyzqvebcxixgkrwragqbhulpuvjraa","qhzgbpatnvllulfuwsjsevkjxymwgdmhrwhnewpozfkmkawfbg","hzeyomccnpqrqeqvmfhxotzjqypnwdjqxkisygdbunovhhceip","niiakmawtltojfcnditvbzbyszzokvjkttgesvgzacddbcbklq","ycrkmnfytayjygltgahkqlwukdnpuehvosfwsoiqgsaftkebzx","zurefhcdiphcwphlqvidpuazpqrscvhneltwajgbfnvswdgqym","trqijdasawfuopnphgdnoppskemryhirbkcxslnokyjjlxafpq","ircduzbnkalhrrqrgghectjyhtwkbrvacajigogcbcoouinoep","uexoqongufysasqfuhsqyjwdkfuvrbrclyhmvevuixoarrlcry","gzxshwcrqagaxratymvpbawofocscerjuuwinktspakyrxjhbn","fkafaqyuopinjihukhtnkcuogpjoilxjsvhbesiyeaketbgrmr","ircduzbnkalhrrqrgghectjyhtwjbrvasajigogcbcoouinoep","qdfkjssmolmrtfbwqvujuzvdilovfldcnqlqddgfhvuuecoida","medazzacwftbfrsgxrbjsauydlooythinpoycmyvrdrgzvxlkb","zcnaiyrgpooyivxsfcpjwjfilixacexfztfnnuxqnvefekjipe","jawmpuxdtrhzqdakjijgwosnkrfbsaaastljdcsspiwhlraggf","cqjaalvdapfmdnhfqakrxkuqzoslkwmoyrxsqkblotnjpubqxb","mleygisvzpziinzfyqtsphmheshpuzouwsuevsogbxdreccywq","ixfkoqzqtnrynuztnknrvmmpzdcpxrzlqjqrkgsxsfghkfftit","xnsfvxjoprekzahmqwptjjercrloyrumfozjdufutxlxocaypx","lulcqtyxrohsisglrbpscrdginwsbayxovxbuthadxudozwtov","rrcwdhinhqxxbeplvoktfurwyrigubdxlbjobvwzbvblahvspb"], ["zuhnxabjbadguzjpambopobdonypauizoxsawbuxoxdvfagryv","pzotsrehcfjrtnauqyubbfnubziuiiykbwwtpghyzyjlhjolqg","khqyzwdxjvcdnutvtvrjcmhsutpqmdcldxazbnypdjehxuzzuz","hbidskugbnkpjrjhtdalregqulzovytzuurwtzckjfxlzxawjr","bljsxqswznxavvfxtgdorfqtwyjsokhuhofzukobjorothlvjm","cdmirnuahenjyxxahsrnhgovxaebnaipxmtkonymnauryplhlv","nitwpyivxagoabmgvnwwswaxiqdozgsocmbfnkfybfhotxeeyf","dfivpnxqpoozszjehbyylpwhxdjswrwmaeujinywekdwzxqagd","kugfxuygumtcningtxqelgcrccrxwhlvrijtebonbxpdtyaolw","ecsyscamxcfjtloukbdilkeajifhubvsdackqypffxcaawjock","sdwngvzrlxunctjtmehzyeamjdqzxmsxvipkvvqyxevzpzjlrv","unnvyubcglfuvdxhyspvfgdszazjbwezjqrygzhdybfahxjtyu","ixfkoqzqtnrynuztnknrvmmpzdcpxrzlqjqskgsxsfghkfftit","qabwqdiinmxjeovkdzytbfefnjisagqgzrnuijlvhnrhrayoxv","ddsrjjzzgnttchwoevrhveprhzvfkyiiwxxvcslubduohuzfye","xzpibujfouyjgmpojmkornixzcakzkarewxljuuiqbctnuvxna","ypindizghzrngzizlrjozspdvadxrgbanvknmecbnqgskkveoz","pylpigvhsexvhjuwvvrvzcnaiasadqknphnfpahwculffowpjt","niiakmawtltojfcnditvbzbyszzokvjkttgesvgzfcddbcbklq","udxuygtxltxtzvatzyxztcjhgtwghkbghkwswsgdeglqgiqxdo","kynhlapvrcucibtgzjyrtzzcjzblkjstuyyprvzgjlkyvlifqt","xmqyfuljgreucigcwrbuzrcqxrmpamvxkjdbqxvegonskawhrs","jelvxblznawvvwdsxtupkhhnjmiebciwwogienkuxwwhxtyimg","ircduzbnkalhrrqrgghectjyhtwkbrvasajigogcbcoouinoep","pdldcqfktmfwojkvjraxmscgwsfumrlwanyjlfbqjeiqvnzsmt","lauobnpapeclnfszbgwitusggzumjhrqqjqxzxktedmnltmoyv","gzxshwcrqagaxratymvpbawofocslerjuuwinktspakyrxjhbn","arnwwbibrqcvwtmekyxoumlfxfbcvkasdyivrzjoswvczrcakj","qhzgbpatmvllulfuwsjsevkjxymwgdmhrwhnewpozfkmkawfbg","haodbfbeqwbyawvtmhxhtbtuihnwzweaxlpnvpwtwoxgpdnibl","wqlafdzvyurcjnjlwadtffhihsvljivfgcqdateimbdykgehqd","mpuaekxvrzwfylwccvejgapiafldlpstsxzbxhxzrbmlgiufdm","wgtwakpwsjdjzazqecosiewqiqlcbzgelwpplglkfxvqiluwrk","zocxuscwwmqcdchovaefttynqsvsmvxdaybyevmhaeqbcjnsdn","szqntzmkdakjmmrhjihdmotknjqhtmlqpcvbboxujiydeqydyk","juyifbniaxwheqrbklorxxwqmwiszqchpzwfcyahtogpkxhfly","uodozsixxzzlulnzixwmospeuewnptmbguoaaloxqgxpzmqbot","neppqmuanqeoqcejqynykxhwxjerabbpbnsbqbzuvlpembevvt","pfcasplzexhutpxazjsfarbozibgoaldyajomicqeehrplbhed","idceltsgkfasypzzlyetuffaxnjufabdqwhgwhrezedjsrofwo","rrcwdhinhqxxueplvoktfurwyrigubdxlbjobvwzbvblahvspb","frqahfkzqyuapowviknpswmaxyctitbcsrbaxglxkxyyqlvddo","zavbrdrlswzrwhdboajmodsyjplrnidjevrhwhocylrmnwnavn","hhkaymbfhwxgdfssnjtsnyzzbxlaheyutiduvcyxbutafmspdw","zqtefyvrsstxlzvdbshmejhodkgxoviojtqufzwdtwsiznbwwk","bastxynudyydwpvwsghcqnapwhdaugoimfbtrsmfwqydoniknx","jlpecoqglgbcpvdbvwnkfixnbojvhrrgamsmxnbxloulstffsj","vzbstfswityijotcezxqvulyneaptcozxqxohdrsdredoyvczw","ectjkbsqnyowofdmjgowpmxtmczxsksepvgjxubklultkdjbkp","fkpmykmbfkwroqmdbjpytzyhpeltlqxertdqkobtoopbcxsclg","lweooqlngaqfggbjeetsuxhqjjtnpoashbynjltbuugqmqcefw","tajdwpsbyuqndarzdlptosugbtapxoxmssxcocmsqyborcxulr","jjljphzrznwdwmmksqllfnsmsoerhykgpbktidcjrorwskxbfp","kysqkpgksxitpndkgrefymvuoxcffketnxjaahsccibpqzhizx","csqndwfzrozscttzqgidpwsobxsgfjtewmcugwmafpgexcfkbr","cqdtundxsgyzfiotczlofgfjvxdlrmszipjesbzgiapmyquauo","vupdbqwhyeqcflxkfoyvpjipupleffytmqgvwhgkafstdtapxa","hepvwxqriomklhanmmyoyzjqxepoydxtjwzakeybfpmgrqlwsa","fdsqfvlssfaylzhjddaosuocwvuciglvrfjtlltalwssfgnpfv","wstbvuaeciraavpzuqaeqguuripkycmfzpewgicyigtzpbbluq","cvofgerjwhzclxsnistliwugxvuccopyetcxjtqkvlnnwaoxpq","ueyoqongufysasqfuhsqyjwdkfuvrbrclyhmvevuixoarrlcry","vcqxolgrmortxthtxpcrfrslpxivuauseqephayzktfjggznvf","erztbvnjgnekygjxyuktbyzqvebcxixgkrwragqbhulpuvjraa","iggmmqoemrfokwzjmvpnmuldfnpzqofugevsinjkdunwaxnyzb","ytfnonxogxgokqshhovfcuwhdombagxplvfeuzmamxrwnfwfaa","mqudaybchpphtbliexdyyqmssydbwunloejdevpuzukclberyd","dsizzlabfylucmendlqqutofzefkewgidpblaqausnqozplrpm","luqgfvyviamlrrhzhvoscxqirvcnooiajsuoxswrbrmzcvailo","cqjaalvdagfmdnhfqakrxkuqzoslkwmoyrxsqkblotnjpubqxb","zjhftehpokrvjwqhmifoqufvhkczmfqigfeakorxhlcdbqmypq","hctmsxooltmuywadnvpulimvunvbxefkvxcwfvicwvldadacxb","cgzuofbuqeqtyrrqiltcnmtglgyokowbgkxkfdppthrohffxsz","gdnmrooojrykspegagdyvkgjviknaxifmyaxwvjsuobzgovnoo","yglzexzciybnrokzogifsrcchxfwdchlzcnfcausalqgrtpeuc","phygwertqjlmzjumzmxrkkizxsfhvztswzsirbclbrvvxmopea","iybpoluezexbjdeifscdtoulbtdwzaoevxtcvsdpwsglsjwcic","ycrkmnfytayjygldgahkqlwukdnpuehvosfwsoiqgsaftkebzx","axakrcmpemovnwjlvnljsxqltwymubcnyabbnqeuyztknokqfv","mwjyjsduczbsnjauipkrcwdkdzegtjdmekfazwviplgagrjyrc","mjosdfmwwrwegbufwektfigzlmttsnoosblwouvozsmdifbebz","bqttutwhumuuvuailmwyxwyazsaseokdcczjyetlvivggajpuv","appytfyqpmhwegjraxldjvuooatolumffxtaknfivqlenldnjc"]))