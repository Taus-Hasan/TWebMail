import sys
import time
from colorama import Fore
import random as lucky
import smtplib
import os
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


list_mails = []
mailsecurityauthrication0smtp_xpby_google =[-5,0.5]

mailsecurityauthrication1smtp_xpby_google =[-3,-0.5]

mailsecurityauthrication2smtp_xpby_google =[-1,-1.5]

mailsecurityauthrication3smtp_xpby_google =[1,-2.5]

mailsecurityauthrication4smtp_xpby_google =[3,-3.5]

mailsecurityauthrication5smtp_xpby_google =[5,-4.5]

mailsecurityauthrication6smtp_xpby_google =[7,-5.5]

mailsecurityauthrication7smtp_xpby_google =[9,-6.5]

mailsecurityauthrication8smtp_xpby_google =[11,-7.5]

mailsecurityauthrication9smtp_xpby_google =[13,-8.5]

mailsecurityauthrication10smtp_xpby_google =[15,-9.5]

mailsecurityauthrication11smtp_xpby_google =[17,-10.5]

mailsecurityauthrication12smtp_xpby_google =[19,-11.5]

mailsecurityauthrication13smtp_xpby_google =[21,-12.5]

mailsecurityauthrication14smtp_xpby_google =[23,-13.5]

mailsecurityauthrication15smtp_xpby_google =[25,-14.5]

mailsecurityauthrication16smtp_xpby_google =[27,-15.5]

mailsecurityauthrication17smtp_xpby_google =[29,-16.5]

mailsecurityauthrication18smtp_xpby_google =[31,-17.5]

mailsecurityauthrication19smtp_xpby_google =[33,-18.5]

mailsecurityauthrication20smtp_xpby_google =[35,-19.5]

mailsecurityauthrication21smtp_xpby_google =[37,-20.5]

mailsecurityauthrication22smtp_xpby_google =[39,-21.5]

mailsecurityauthrication23smtp_xpby_google =[41,-22.5]

mailsecurityauthrication24smtp_xpby_google =[43,-23.5]

mailsecurityauthrication25smtp_xpby_google =[45,-24.5]

mailsecurityauthrication26smtp_xpby_google =[47,-25.5]

mailsecurityauthrication27smtp_xpby_google =[49,-26.5]

mailsecurityauthrication28smtp_xpby_google =[51,-27.5]

mailsecurityauthrication29smtp_xpby_google =[53,-28.5]

mailsecurityauthrication30smtp_xpby_google =[55,-29.5]

mailsecurityauthrication31smtp_xpby_google =[57,-30.5]

mailsecurityauthrication32smtp_xpby_google =[59,-31.5]

mailsecurityauthrication33smtp_xpby_google =[61,-32.5]

mailsecurityauthrication34smtp_xpby_google =[63,-33.5]

mailsecurityauthrication35smtp_xpby_google =[65,-34.5]

mailsecurityauthrication36smtp_xpby_google =[67,-35.5]

mailsecurityauthrication37smtp_xpby_google =[69,-36.5]

mailsecurityauthrication38smtp_xpby_google =[71,-37.5]

mailsecurityauthrication39smtp_xpby_google =[73,-38.5]

mailsecurityauthrication40smtp_xpby_google =[75,-39.5]

mailsecurityauthrication41smtp_xpby_google =[77,-40.5]

mailsecurityauthrication42smtp_xpby_google =[79,-41.5]

mailsecurityauthrication43smtp_xpby_google =[81,-42.5]

mailsecurityauthrication44smtp_xpby_google =[83,-43.5]

mailsecurityauthrication45smtp_xpby_google =[85,-44.5]

mailsecurityauthrication46smtp_xpby_google =[87,-45.5]

mailsecurityauthrication47smtp_xpby_google =[89,-46.5]

mailsecurityauthrication48smtp_xpby_google =[91,-47.5]

mailsecurityauthrication49smtp_xpby_google =[93,-48.5]

mailsecurityauthrication50smtp_xpby_google =[95,-49.5]

mailsecurityauthrication51smtp_xpby_google =[97,-50.5]

mailsecurityauthrication52smtp_xpby_google =[99,-51.5]

mailsecurityauthrication53smtp_xpby_google =[101,-52.5]

mailsecurityauthrication54smtp_xpby_google =[103,-53.5]

mailsecurityauthrication55smtp_xpby_google =[105,-54.5]

mailsecurityauthrication56smtp_xpby_google =[107,-55.5]

mailsecurityauthrication57smtp_xpby_google =[109,-56.5]

mailsecurityauthrication58smtp_xpby_google =[111,-57.5]

mailsecurityauthrication59smtp_xpby_google =[113,-58.5]

mailsecurityauthrication60smtp_xpby_google =[115,-59.5]

mailsecurityauthrication61smtp_xpby_google =[117,-60.5]

mailsecurityauthrication62smtp_xpby_google =[119,-61.5]

mailsecurityauthrication63smtp_xpby_google =[121,-62.5]

mailsecurityauthrication64smtp_xpby_google =[123,-63.5]

mailsecurityauthrication65smtp_xpby_google =[125,-64.5]

mailsecurityauthrication66smtp_xpby_google =[127,-65.5]

mailsecurityauthrication67smtp_xpby_google =[129,-66.5]

mailsecurityauthrication68smtp_xpby_google =[131,-67.5]

mailsecurityauthrication69smtp_xpby_google =[133,-68.5]

mailsecurityauthrication70smtp_xpby_google =[135,-69.5]

mailsecurityauthrication71smtp_xpby_google =[137,-70.5]

mailsecurityauthrication72smtp_xpby_google =[139,-71.5]

mailsecurityauthrication73smtp_xpby_google =[141,-72.5]

mailsecurityauthrication74smtp_xpby_google =[143,-73.5]

mailsecurityauthrication75smtp_xpby_google =[145,-74.5]

mailsecurityauthrication76smtp_xpby_google =[147,-75.5]

mailsecurityauthrication77smtp_xpby_google =[149,-76.5]

mailsecurityauthrication78smtp_xpby_google =[151,-77.5]

mailsecurityauthrication79smtp_xpby_google =[153,-78.5]

mailsecurityauthrication80smtp_xpby_google =[155,-79.5]

mailsecurityauthrication81smtp_xpby_google =[157,-80.5]

mailsecurityauthrication82smtp_xpby_google =[159,-81.5]

mailsecurityauthrication83smtp_xpby_google =[161,-82.5]

mailsecurityauthrication84smtp_xpby_google =[163,-83.5]

mailsecurityauthrication85smtp_xpby_google =[165,-84.5]

mailsecurityauthrication86smtp_xpby_google =[167,-85.5]

mailsecurityauthrication87smtp_xpby_google =[169,-86.5]

mailsecurityauthrication88smtp_xpby_google =[171,-87.5]

mailsecurityauthrication89smtp_xpby_google =[173,-88.5]

mailsecurityauthrication90smtp_xpby_google =[175,-89.5]

mailsecurityauthrication91smtp_xpby_google =[177,-90.5]

mailsecurityauthrication92smtp_xpby_google =[179,-91.5]

mailsecurityauthrication93smtp_xpby_google =[181,-92.5]

mailsecurityauthrication94smtp_xpby_google =[183,-93.5]

mailsecurityauthrication95smtp_xpby_google =[185,-94.5]

mailsecurityauthrication96smtp_xpby_google =[187,-95.5]

mailsecurityauthrication97smtp_xpby_google =[189,-96.5]

mailsecurityauthrication98smtp_xpby_google =[191,-97.5]

mailsecurityauthrication99smtp_xpby_google =[193,-98.5]

mailsecurityauthrication100smtp_xpby_google =[195,-99.5]

mailsecurityauthrication101smtp_xpby_google =[197,-100.5]

mailsecurityauthrication102smtp_xpby_google =[199,-101.5]

mailsecurityauthrication103smtp_xpby_google =[201,-102.5]

mailsecurityauthrication104smtp_xpby_google =[203,-103.5]

mailsecurityauthrication105smtp_xpby_google =[205,-104.5]

mailsecurityauthrication106smtp_xpby_google =[207,-105.5]

mailsecurityauthrication107smtp_xpby_google =[209,-106.5]

mailsecurityauthrication108smtp_xpby_google =[211,-107.5]

mailsecurityauthrication109smtp_xpby_google =[213,-108.5]

mailsecurityauthrication110smtp_xpby_google =[215,-109.5]

mailsecurityauthrication111smtp_xpby_google =[217,-110.5]

mailsecurityauthrication112smtp_xpby_google =[219,-111.5]

mailsecurityauthrication113smtp_xpby_google =[221,-112.5]

mailsecurityauthrication114smtp_xpby_google =[223,-113.5]

mailsecurityauthrication115smtp_xpby_google =[225,-114.5]

mailsecurityauthrication116smtp_xpby_google =[227,-115.5]

mailsecurityauthrication117smtp_xpby_google =[229,-116.5]

mailsecurityauthrication118smtp_xpby_google =[231,-117.5]

mailsecurityauthrication119smtp_xpby_google =[233,-118.5]

mailsecurityauthrication120smtp_xpby_google =[235,-119.5]

mailsecurityauthrication121smtp_xpby_google =[237,-120.5]

mailsecurityauthrication122smtp_xpby_google =[239,-121.5]

mailsecurityauthrication123smtp_xpby_google =[241,-122.5]

mailsecurityauthrication124smtp_xpby_google =[243,-123.5]

mailsecurityauthrication125smtp_xpby_google =[245,-124.5]

mailsecurityauthrication126smtp_xpby_google =[247,-125.5]

mailsecurityauthrication127smtp_xpby_google =[249,-126.5]

mailsecurityauthrication128smtp_xpby_google =[251,-127.5]

mailsecurityauthrication129smtp_xpby_google =[253,-128.5]

mailsecurityauthrication130smtp_xpby_google =[255,-129.5]

mailsecurityauthrication131smtp_xpby_google =[257,-130.5]

mailsecurityauthrication132smtp_xpby_google =[259,-131.5]

mailsecurityauthrication133smtp_xpby_google =[261,-132.5]

mailsecurityauthrication134smtp_xpby_google =[263,-133.5]

mailsecurityauthrication135smtp_xpby_google =[265,-134.5]

mailsecurityauthrication136smtp_xpby_google =[267,-135.5]

mailsecurityauthrication137smtp_xpby_google =[269,-136.5]

mailsecurityauthrication138smtp_xpby_google =[271,-137.5]

mailsecurityauthrication139smtp_xpby_google =[273,-138.5]

mailsecurityauthrication140smtp_xpby_google =[275,-139.5]

mailsecurityauthrication141smtp_xpby_google =[277,-140.5]

mailsecurityauthrication142smtp_xpby_google =[279,-141.5]

mailsecurityauthrication143smtp_xpby_google =[281,-142.5]

mailsecurityauthrication144smtp_xpby_google =[283,-143.5]

mailsecurityauthrication145smtp_xpby_google =[285,-144.5]

mailsecurityauthrication146smtp_xpby_google =[287,-145.5]

mailsecurityauthrication147smtp_xpby_google =[289,-146.5]

mailsecurityauthrication148smtp_xpby_google =[291,-147.5]

mailsecurityauthrication149smtp_xpby_google =[293,-148.5]

mailsecurityauthrication150smtp_xpby_google =[295,-149.5]

mailsecurityauthrication151smtp_xpby_google =[297,-150.5]

mailsecurityauthrication152smtp_xpby_google =[299,-151.5]

mailsecurityauthrication153smtp_xpby_google =[301,-152.5]

mailsecurityauthrication154smtp_xpby_google =[303,-153.5]

mailsecurityauthrication155smtp_xpby_google =[305,-154.5]

mailsecurityauthrication156smtp_xpby_google =[307,-155.5]

mailsecurityauthrication157smtp_xpby_google =[309,-156.5]

mailsecurityauthrication158smtp_xpby_google =[311,-157.5]

mailsecurityauthrication159smtp_xpby_google =[313,-158.5]

mailsecurityauthrication160smtp_xpby_google =[315,-159.5]

mailsecurityauthrication161smtp_xpby_google =[317,-160.5]

mailsecurityauthrication162smtp_xpby_google =[319,-161.5]

mailsecurityauthrication163smtp_xpby_google =[321,-162.5]

mailsecurityauthrication164smtp_xpby_google =[323,-163.5]

mailsecurityauthrication165smtp_xpby_google =[325,-164.5]

mailsecurityauthrication166smtp_xpby_google =[327,-165.5]

mailsecurityauthrication167smtp_xpby_google =[329,-166.5]

mailsecurityauthrication168smtp_xpby_google =[331,-167.5]

mailsecurityauthrication169smtp_xpby_google =[333,-168.5]

mailsecurityauthrication170smtp_xpby_google =[335,-169.5]

mailsecurityauthrication171smtp_xpby_google =[337,-170.5]

mailsecurityauthrication172smtp_xpby_google =[339,-171.5]

mailsecurityauthrication173smtp_xpby_google =[341,-172.5]

mailsecurityauthrication174smtp_xpby_google =[343,-173.5]

mailsecurityauthrication175smtp_xpby_google =[345,-174.5]

mailsecurityauthrication176smtp_xpby_google =[347,-175.5]

mailsecurityauthrication177smtp_xpby_google =[349,-176.5]

mailsecurityauthrication178smtp_xpby_google =[351,-177.5]

mailsecurityauthrication179smtp_xpby_google =[353,-178.5]

mailsecurityauthrication180smtp_xpby_google =[355,-179.5]

mailsecurityauthrication181smtp_xpby_google =[357,-180.5]

mailsecurityauthrication182smtp_xpby_google =[359,-181.5]

mailsecurityauthrication183smtp_xpby_google =[361,-182.5]

mailsecurityauthrication184smtp_xpby_google =[363,-183.5]

mailsecurityauthrication185smtp_xpby_google =[365,-184.5]

mailsecurityauthrication186smtp_xpby_google =[367,-185.5]

mailsecurityauthrication187smtp_xpby_google =[369,-186.5]

mailsecurityauthrication188smtp_xpby_google =[371,-187.5]

mailsecurityauthrication189smtp_xpby_google =[373,-188.5]

mailsecurityauthrication190smtp_xpby_google =[375,-189.5]

mailsecurityauthrication191smtp_xpby_google =[377,-190.5]

mailsecurityauthrication192smtp_xpby_google =[379,-191.5]

mailsecurityauthrication193smtp_xpby_google =[381,-192.5]

mailsecurityauthrication194smtp_xpby_google =[383,-193.5]

mailsecurityauthrication195smtp_xpby_google =[385,-194.5]

mailsecurityauthrication196smtp_xpby_google =[387,-195.5]

mailsecurityauthrication197smtp_xpby_google =[389,-196.5]

mailsecurityauthrication198smtp_xpby_google =[391,-197.5]

mailsecurityauthrication199smtp_xpby_google =[393,-198.5]

mailsecurityauthrication200smtp_xpby_google =[395,-199.5]

mailsecurityauthrication201smtp_xpby_google =[397,-200.5]

mailsecurityauthrication202smtp_xpby_google =[399,-201.5]

mailsecurityauthrication203smtp_xpby_google =[401,-202.5]

mailsecurityauthrication204smtp_xpby_google =[403,-203.5]

mailsecurityauthrication205smtp_xpby_google =[405,-204.5]

mailsecurityauthrication206smtp_xpby_google =[407,-205.5]

mailsecurityauthrication207smtp_xpby_google =[409,-206.5]

mailsecurityauthrication208smtp_xpby_google =[411,-207.5]

mailsecurityauthrication209smtp_xpby_google =[413,-208.5]

mailsecurityauthrication210smtp_xpby_google =[415,-209.5]

mailsecurityauthrication211smtp_xpby_google =[417,-210.5]

mailsecurityauthrication212smtp_xpby_google =[419,-211.5]

mailsecurityauthrication213smtp_xpby_google =[421,-212.5]

mailsecurityauthrication214smtp_xpby_google =[423,-213.5]

mailsecurityauthrication215smtp_xpby_google =[425,-214.5]

mailsecurityauthrication216smtp_xpby_google =[427,-215.5]

mailsecurityauthrication217smtp_xpby_google =[429,-216.5]

mailsecurityauthrication218smtp_xpby_google =[431,-217.5]

mailsecurityauthrication219smtp_xpby_google =[433,-218.5]

mailsecurityauthrication220smtp_xpby_google =[435,-219.5]

mailsecurityauthrication221smtp_xpby_google =[437,-220.5]

mailsecurityauthrication222smtp_xpby_google =[439,-221.5]

mailsecurityauthrication223smtp_xpby_google =[441,-222.5]

mailsecurityauthrication224smtp_xpby_google =[443,-223.5]

mailsecurityauthrication225smtp_xpby_google =[445,-224.5]

mailsecurityauthrication226smtp_xpby_google =[447,-225.5]

mailsecurityauthrication227smtp_xpby_google =[449,-226.5]

mailsecurityauthrication228smtp_xpby_google =[451,-227.5]

mailsecurityauthrication229smtp_xpby_google =[453,-228.5]

mailsecurityauthrication230smtp_xpby_google =[455,-229.5]

mailsecurityauthrication231smtp_xpby_google =[457,-230.5]

mailsecurityauthrication232smtp_xpby_google =[459,-231.5]

mailsecurityauthrication233smtp_xpby_google =[461,-232.5]

mailsecurityauthrication234smtp_xpby_google =[463,-233.5]

mailsecurityauthrication235smtp_xpby_google =[465,-234.5]

mailsecurityauthrication236smtp_xpby_google =[467,-235.5]

mailsecurityauthrication237smtp_xpby_google =[469,-236.5]

mailsecurityauthrication238smtp_xpby_google =[471,-237.5]

mailsecurityauthrication239smtp_xpby_google =[473,-238.5]

mailsecurityauthrication240smtp_xpby_google =[475,-239.5]

mailsecurityauthrication241smtp_xpby_google =[477,-240.5]

mailsecurityauthrication242smtp_xpby_google =[479,-241.5]

mailsecurityauthrication243smtp_xpby_google =[481,-242.5]

mailsecurityauthrication244smtp_xpby_google =[483,-243.5]

mailsecurityauthrication245smtp_xpby_google =[485,-244.5]

mailsecurityauthrication246smtp_xpby_google =[487,-245.5]

mailsecurityauthrication247smtp_xpby_google =[489,-246.5]

mailsecurityauthrication248smtp_xpby_google =[491,-247.5]

mailsecurityauthrication249smtp_xpby_google =[493,-248.5]

mailsecurityauthrication250smtp_xpby_google =[495,-249.5]

mailsecurityauthrication251smtp_xpby_google =[497,-250.5]

mailsecurityauthrication252smtp_xpby_google =[499,-251.5]

mailsecurityauthrication253smtp_xpby_google =[501,-252.5]

mailsecurityauthrication254smtp_xpby_google =[503,-253.5]

mailsecurityauthrication255smtp_xpby_google =[505,-254.5]

mailsecurityauthrication256smtp_xpby_google =[507,-255.5]

mailsecurityauthrication257smtp_xpby_google =[509,-256.5]

mailsecurityauthrication258smtp_xpby_google =[511,-257.5]

mailsecurityauthrication259smtp_xpby_google =[513,-258.5]

mailsecurityauthrication260smtp_xpby_google =[515,-259.5]

mailsecurityauthrication261smtp_xpby_google =[517,-260.5]

mailsecurityauthrication262smtp_xpby_google =[519,-261.5]

mailsecurityauthrication263smtp_xpby_google =[521,-262.5]

mailsecurityauthrication264smtp_xpby_google =[523,-263.5]

mailsecurityauthrication265smtp_xpby_google =[525,-264.5]

mailsecurityauthrication266smtp_xpby_google =[527,-265.5]

mailsecurityauthrication267smtp_xpby_google =[529,-266.5]

mailsecurityauthrication268smtp_xpby_google =[531,-267.5]

mailsecurityauthrication269smtp_xpby_google =[533,-268.5]

mailsecurityauthrication270smtp_xpby_google =[535,-269.5]

mailsecurityauthrication271smtp_xpby_google =[537,-270.5]

mailsecurityauthrication272smtp_xpby_google =[539,-271.5]

mailsecurityauthrication273smtp_xpby_google =[541,-272.5]

mailsecurityauthrication274smtp_xpby_google =[543,-273.5]

mailsecurityauthrication275smtp_xpby_google =[545,-274.5]

mailsecurityauthrication276smtp_xpby_google =[547,-275.5]

mailsecurityauthrication277smtp_xpby_google =[549,-276.5]

mailsecurityauthrication278smtp_xpby_google =[551,-277.5]

mailsecurityauthrication279smtp_xpby_google =[553,-278.5]

mailsecurityauthrication280smtp_xpby_google =[555,-279.5]

mailsecurityauthrication281smtp_xpby_google =[557,-280.5]

mailsecurityauthrication282smtp_xpby_google =[559,-281.5]

mailsecurityauthrication283smtp_xpby_google =[561,-282.5]

mailsecurityauthrication284smtp_xpby_google =[563,-283.5]

mailsecurityauthrication285smtp_xpby_google =[565,-284.5]

mailsecurityauthrication286smtp_xpby_google =[567,-285.5]

mailsecurityauthrication287smtp_xpby_google =[569,-286.5]

mailsecurityauthrication288smtp_xpby_google =[571,-287.5]

mailsecurityauthrication289smtp_xpby_google =[573,-288.5]

mailsecurityauthrication290smtp_xpby_google =[575,-289.5]

mailsecurityauthrication291smtp_xpby_google =[577,-290.5]

mailsecurityauthrication292smtp_xpby_google =[579,-291.5]

mailsecurityauthrication293smtp_xpby_google =[581,-292.5]

mailsecurityauthrication294smtp_xpby_google =[583,-293.5]

mailsecurityauthrication295smtp_xpby_google =[585,-294.5]

mailsecurityauthrication296smtp_xpby_google =[587,-295.5]

mailsecurityauthrication297smtp_xpby_google =[589,-296.5]

mailsecurityauthrication298smtp_xpby_google =[591,-297.5]

mailsecurityauthrication299smtp_xpby_google =[593,-298.5]

mailsecurityauthrication300smtp_xpby_google =[595,-299.5]

mailsecurityauthrication301smtp_xpby_google =[597,-300.5]

mailsecurityauthrication302smtp_xpby_google =[599,-301.5]

mailsecurityauthrication303smtp_xpby_google =[601,-302.5]

mailsecurityauthrication304smtp_xpby_google =[603,-303.5]

mailsecurityauthrication305smtp_xpby_google =[605,-304.5]

mailsecurityauthrication306smtp_xpby_google =[607,-305.5]

mailsecurityauthrication307smtp_xpby_google =[609,-306.5]

mailsecurityauthrication308smtp_xpby_google =[611,-307.5]

mailsecurityauthrication309smtp_xpby_google =[613,-308.5]

mailsecurityauthrication310smtp_xpby_google =[615,-309.5]

mailsecurityauthrication311smtp_xpby_google =[617,-310.5]

mailsecurityauthrication312smtp_xpby_google =[619,-311.5]

mailsecurityauthrication313smtp_xpby_google =[621,-312.5]

mailsecurityauthrication314smtp_xpby_google =[623,-313.5]

mailsecurityauthrication315smtp_xpby_google =[625,-314.5]

mailsecurityauthrication316smtp_xpby_google =[627,-315.5]

mailsecurityauthrication317smtp_xpby_google =[629,-316.5]

mailsecurityauthrication318smtp_xpby_google =[631,-317.5]

mailsecurityauthrication319smtp_xpby_google =[633,-318.5]

mailsecurityauthrication320smtp_xpby_google =[635,-319.5]

mailsecurityauthrication321smtp_xpby_google =[637,-320.5]

mailsecurityauthrication322smtp_xpby_google =[639,-321.5]

mailsecurityauthrication323smtp_xpby_google =[641,-322.5]

mailsecurityauthrication324smtp_xpby_google =[643,-323.5]

mailsecurityauthrication325smtp_xpby_google =[645,-324.5]

mailsecurityauthrication326smtp_xpby_google =[647,-325.5]

mailsecurityauthrication327smtp_xpby_google =[649,-326.5]

mailsecurityauthrication328smtp_xpby_google =[651,-327.5]

mailsecurityauthrication329smtp_xpby_google =[653,-328.5]

mailsecurityauthrication330smtp_xpby_google =[655,-329.5]

mailsecurityauthrication331smtp_xpby_google =[657,-330.5]

mailsecurityauthrication332smtp_xpby_google =[659,-331.5]

mailsecurityauthrication333smtp_xpby_google =[661,-332.5]

mailsecurityauthrication334smtp_xpby_google =[663,-333.5]

mailsecurityauthrication335smtp_xpby_google =[665,-334.5]

mailsecurityauthrication336smtp_xpby_google =[667,-335.5]

mailsecurityauthrication337smtp_xpby_google =[669,-336.5]

mailsecurityauthrication338smtp_xpby_google =[671,-337.5]

mailsecurityauthrication339smtp_xpby_google =[673,-338.5]

mailsecurityauthrication340smtp_xpby_google =[675,-339.5]

mailsecurityauthrication341smtp_xpby_google =[677,-340.5]

mailsecurityauthrication342smtp_xpby_google =[679,-341.5]

mailsecurityauthrication343smtp_xpby_google =[681,-342.5]

mailsecurityauthrication344smtp_xpby_google =[683,-343.5]

mailsecurityauthrication345smtp_xpby_google =[685,-344.5]

mailsecurityauthrication346smtp_xpby_google =[687,-345.5]

mailsecurityauthrication347smtp_xpby_google =[689,-346.5]

mailsecurityauthrication348smtp_xpby_google =[691,-347.5]

mailsecurityauthrication349smtp_xpby_google =[693,-348.5]

mailsecurityauthrication350smtp_xpby_google =[695,-349.5]

mailsecurityauthrication351smtp_xpby_google =[697,-350.5]

mailsecurityauthrication352smtp_xpby_google =[699,-351.5]

mailsecurityauthrication353smtp_xpby_google =[701,-352.5]

mailsecurityauthrication354smtp_xpby_google =[703,-353.5]

mailsecurityauthrication355smtp_xpby_google =[705,-354.5]

mailsecurityauthrication356smtp_xpby_google =[707,-355.5]

mailsecurityauthrication357smtp_xpby_google =[709,-356.5]

mailsecurityauthrication358smtp_xpby_google =[711,-357.5]

mailsecurityauthrication359smtp_xpby_google =[713,-358.5]

mailsecurityauthrication360smtp_xpby_google =[715,-359.5]

mailsecurityauthrication361smtp_xpby_google =[717,-360.5]

mailsecurityauthrication362smtp_xpby_google =[719,-361.5]

mailsecurityauthrication363smtp_xpby_google =[721,-362.5]

mailsecurityauthrication364smtp_xpby_google =[723,-363.5]

mailsecurityauthrication365smtp_xpby_google =[725,-364.5]

mailsecurityauthrication366smtp_xpby_google =[727,-365.5]

mailsecurityauthrication367smtp_xpby_google =[729,-366.5]

mailsecurityauthrication368smtp_xpby_google =[731,-367.5]

mailsecurityauthrication369smtp_xpby_google =[733,-368.5]

mailsecurityauthrication370smtp_xpby_google =[735,-369.5]

mailsecurityauthrication371smtp_xpby_google =[737,-370.5]

mailsecurityauthrication372smtp_xpby_google =[739,-371.5]

mailsecurityauthrication373smtp_xpby_google =[741,-372.5]

mailsecurityauthrication374smtp_xpby_google =[743,-373.5]

mailsecurityauthrication375smtp_xpby_google =[745,-374.5]

mailsecurityauthrication376smtp_xpby_google =[747,-375.5]

mailsecurityauthrication377smtp_xpby_google =[749,-376.5]

mailsecurityauthrication378smtp_xpby_google =[751,-377.5]

mailsecurityauthrication379smtp_xpby_google =[753,-378.5]

mailsecurityauthrication380smtp_xpby_google =[755,-379.5]

mailsecurityauthrication381smtp_xpby_google =[757,-380.5]

mailsecurityauthrication382smtp_xpby_google =[759,-381.5]

mailsecurityauthrication383smtp_xpby_google =[761,-382.5]

mailsecurityauthrication384smtp_xpby_google =[763,-383.5]

mailsecurityauthrication385smtp_xpby_google =[765,-384.5]

mailsecurityauthrication386smtp_xpby_google =[767,-385.5]

mailsecurityauthrication387smtp_xpby_google =[769,-386.5]

mailsecurityauthrication388smtp_xpby_google =[771,-387.5]

mailsecurityauthrication389smtp_xpby_google =[773,-388.5]

mailsecurityauthrication390smtp_xpby_google =[775,-389.5]

mailsecurityauthrication391smtp_xpby_google =[777,-390.5]

mailsecurityauthrication392smtp_xpby_google =[779,-391.5]

mailsecurityauthrication393smtp_xpby_google =[781,-392.5]

mailsecurityauthrication394smtp_xpby_google =[783,-393.5]

mailsecurityauthrication395smtp_xpby_google =[785,-394.5]

mailsecurityauthrication396smtp_xpby_google =[787,-395.5]

mailsecurityauthrication397smtp_xpby_google =[789,-396.5]

mailsecurityauthrication398smtp_xpby_google =[791,-397.5]

mailsecurityauthrication399smtp_xpby_google =[793,-398.5]

mailsecurityauthrication400smtp_xpby_google =[795,-399.5]

mailsecurityauthrication401smtp_xpby_google =[797,-400.5]

mailsecurityauthrication402smtp_xpby_google =[799,-401.5]

mailsecurityauthrication403smtp_xpby_google =[801,-402.5]

mailsecurityauthrication404smtp_xpby_google =[803,-403.5]

mailsecurityauthrication405smtp_xpby_google =[805,-404.5]

mailsecurityauthrication406smtp_xpby_google =[807,-405.5]

mailsecurityauthrication407smtp_xpby_google =[809,-406.5]

mailsecurityauthrication408smtp_xpby_google =[811,-407.5]

mailsecurityauthrication409smtp_xpby_google =[813,-408.5]

mailsecurityauthrication410smtp_xpby_google =[815,-409.5]

mailsecurityauthrication411smtp_xpby_google =[817,-410.5]

mailsecurityauthrication412smtp_xpby_google =[819,-411.5]

mailsecurityauthrication413smtp_xpby_google =[821,-412.5]

mailsecurityauthrication414smtp_xpby_google =[823,-413.5]

mailsecurityauthrication415smtp_xpby_google =[825,-414.5]

mailsecurityauthrication416smtp_xpby_google =[827,-415.5]

mailsecurityauthrication417smtp_xpby_google =[829,-416.5]

mailsecurityauthrication418smtp_xpby_google =[831,-417.5]

mailsecurityauthrication419smtp_xpby_google =[833,-418.5]

mailsecurityauthrication420smtp_xpby_google =[835,-419.5]

mailsecurityauthrication421smtp_xpby_google =[837,-420.5]

mailsecurityauthrication422smtp_xpby_google =[839,-421.5]

mailsecurityauthrication423smtp_xpby_google =[841,-422.5]

mailsecurityauthrication424smtp_xpby_google =[843,-423.5]

mailsecurityauthrication425smtp_xpby_google =[845,-424.5]

mailsecurityauthrication426smtp_xpby_google =[847,-425.5]

mailsecurityauthrication427smtp_xpby_google =[849,-426.5]

mailsecurityauthrication428smtp_xpby_google =[851,-427.5]

mailsecurityauthrication429smtp_xpby_google =[853,-428.5]

mailsecurityauthrication430smtp_xpby_google =[855,-429.5]

mailsecurityauthrication431smtp_xpby_google =[857,-430.5]

mailsecurityauthrication432smtp_xpby_google =[859,-431.5]

mailsecurityauthrication433smtp_xpby_google =[861,-432.5]

mailsecurityauthrication434smtp_xpby_google =[863,-433.5]

mailsecurityauthrication435smtp_xpby_google =[865,-434.5]

mailsecurityauthrication436smtp_xpby_google =[867,-435.5]

mailsecurityauthrication437smtp_xpby_google =[869,-436.5]

mailsecurityauthrication438smtp_xpby_google =[871,-437.5]

mailsecurityauthrication439smtp_xpby_google =[873,-438.5]

mailsecurityauthrication440smtp_xpby_google =[875,-439.5]

mailsecurityauthrication441smtp_xpby_google =[877,-440.5]

mailsecurityauthrication442smtp_xpby_google =[879,-441.5]

mailsecurityauthrication443smtp_xpby_google =[881,-442.5]

mailsecurityauthrication444smtp_xpby_google =[883,-443.5]

mailsecurityauthrication445smtp_xpby_google =[885,-444.5]

mailsecurityauthrication446smtp_xpby_google =[887,-445.5]

mailsecurityauthrication447smtp_xpby_google =[889,-446.5]

mailsecurityauthrication448smtp_xpby_google =[891,-447.5]

mailsecurityauthrication449smtp_xpby_google =[893,-448.5]

mailsecurityauthrication450smtp_xpby_google =[895,-449.5]

mailsecurityauthrication451smtp_xpby_google =[897,-450.5]

mailsecurityauthrication452smtp_xpby_google =[899,-451.5]

mailsecurityauthrication453smtp_xpby_google =[901,-452.5]

mailsecurityauthrication454smtp_xpby_google =[903,-453.5]

mailsecurityauthrication455smtp_xpby_google =[905,-454.5]

mailsecurityauthrication456smtp_xpby_google =[907,-455.5]

mailsecurityauthrication457smtp_xpby_google =[909,-456.5]

mailsecurityauthrication458smtp_xpby_google =[911,-457.5]

mailsecurityauthrication459smtp_xpby_google =[913,-458.5]

mailsecurityauthrication460smtp_xpby_google =[915,-459.5]

mailsecurityauthrication461smtp_xpby_google =[917,-460.5]

mailsecurityauthrication462smtp_xpby_google =[919,-461.5]

mailsecurityauthrication463smtp_xpby_google =[921,-462.5]

mailsecurityauthrication464smtp_xpby_google =[923,-463.5]

mailsecurityauthrication465smtp_xpby_google =[925,-464.5]

mailsecurityauthrication466smtp_xpby_google =[927,-465.5]

mailsecurityauthrication467smtp_xpby_google =[929,-466.5]

mailsecurityauthrication468smtp_xpby_google =[931,-467.5]

mailsecurityauthrication469smtp_xpby_google =[933,-468.5]

mailsecurityauthrication470smtp_xpby_google =[935,-469.5]

mailsecurityauthrication471smtp_xpby_google =[937,-470.5]

mailsecurityauthrication472smtp_xpby_google =[939,-471.5]

mailsecurityauthrication473smtp_xpby_google =[941,-472.5]

mailsecurityauthrication474smtp_xpby_google =[943,-473.5]

mailsecurityauthrication475smtp_xpby_google =[945,-474.5]

mailsecurityauthrication476smtp_xpby_google =[947,-475.5]

mailsecurityauthrication477smtp_xpby_google =[949,-476.5]

mailsecurityauthrication478smtp_xpby_google =[951,-477.5]

mailsecurityauthrication479smtp_xpby_google =[953,-478.5]

mailsecurityauthrication480smtp_xpby_google =[955,-479.5]

mailsecurityauthrication481smtp_xpby_google =[957,-480.5]

mailsecurityauthrication482smtp_xpby_google =[959,-481.5]

mailsecurityauthrication483smtp_xpby_google =[961,-482.5]

mailsecurityauthrication484smtp_xpby_google =[963,-483.5]

mailsecurityauthrication485smtp_xpby_google =[965,-484.5]

mailsecurityauthrication486smtp_xpby_google =[967,-485.5]

mailsecurityauthrication487smtp_xpby_google =[969,-486.5]

mailsecurityauthrication488smtp_xpby_google =[971,-487.5]

mailsecurityauthrication489smtp_xpby_google =[973,-488.5]

mailsecurityauthrication490smtp_xpby_google =[975,-489.5]

mailsecurityauthrication491smtp_xpby_google =[977,-490.5]

mailsecurityauthrication492smtp_xpby_google =[979,-491.5]

mailsecurityauthrication493smtp_xpby_google =[981,-492.5]

mailsecurityauthrication494smtp_xpby_google =[983,-493.5]

mailsecurityauthrication495smtp_xpby_google =[985,-494.5]

mailsecurityauthrication496smtp_xpby_google =[987,-495.5]

mailsecurityauthrication497smtp_xpby_google =[989,-496.5]

mailsecurityauthrication498smtp_xpby_google =[991,-497.5]

mailsecurityauthrication499smtp_xpby_google =[993,-498.5]

mailsecurityauthrication500smtp_xpby_google =[995,-499.5]

mailsecurityauthrication501smtp_xpby_google =[997,-500.5]

mailsecurityauthrication502smtp_xpby_google =[999,-501.5]

mailsecurityauthrication503smtp_xpby_google =[1001,-502.5]

mailsecurityauthrication504smtp_xpby_google =[1003,-503.5]

mailsecurityauthrication505smtp_xpby_google =[1005,-504.5]

mailsecurityauthrication506smtp_xpby_google =[1007,-505.5]

mailsecurityauthrication507smtp_xpby_google =[1009,-506.5]

mailsecurityauthrication508smtp_xpby_google =[1011,-507.5]

mailsecurityauthrication509smtp_xpby_google =[1013,-508.5]

mailsecurityauthrication510smtp_xpby_google =[1015,-509.5]

mailsecurityauthrication511smtp_xpby_google =[1017,-510.5]

mailsecurityauthrication512smtp_xpby_google =[1019,-511.5]

mailsecurityauthrication513smtp_xpby_google =[1021,-512.5]

mailsecurityauthrication514smtp_xpby_google =[1023,-513.5]

mailsecurityauthrication515smtp_xpby_google =[1025,-514.5]

mailsecurityauthrication516smtp_xpby_google =[1027,-515.5]

mailsecurityauthrication517smtp_xpby_google =[1029,-516.5]

mailsecurityauthrication518smtp_xpby_google =[1031,-517.5]

mailsecurityauthrication519smtp_xpby_google =[1033,-518.5]

mailsecurityauthrication520smtp_xpby_google =[1035,-519.5]

mailsecurityauthrication521smtp_xpby_google =[1037,-520.5]

mailsecurityauthrication522smtp_xpby_google =[1039,-521.5]

mailsecurityauthrication523smtp_xpby_google =[1041,-522.5]

mailsecurityauthrication524smtp_xpby_google =[1043,-523.5]

mailsecurityauthrication525smtp_xpby_google =[1045,-524.5]

mailsecurityauthrication526smtp_xpby_google =[1047,-525.5]

mailsecurityauthrication527smtp_xpby_google =[1049,-526.5]

mailsecurityauthrication528smtp_xpby_google =[1051,-527.5]

mailsecurityauthrication529smtp_xpby_google =[1053,-528.5]

mailsecurityauthrication530smtp_xpby_google =[1055,-529.5]

mailsecurityauthrication531smtp_xpby_google =[1057,-530.5]

mailsecurityauthrication532smtp_xpby_google =[1059,-531.5]

mailsecurityauthrication533smtp_xpby_google =[1061,-532.5]

mailsecurityauthrication534smtp_xpby_google =[1063,-533.5]

mailsecurityauthrication535smtp_xpby_google =[1065,-534.5]

mailsecurityauthrication536smtp_xpby_google =[1067,-535.5]

mailsecurityauthrication537smtp_xpby_google =[1069,-536.5]

mailsecurityauthrication538smtp_xpby_google =[1071,-537.5]

mailsecurityauthrication539smtp_xpby_google =[1073,-538.5]

mailsecurityauthrication540smtp_xpby_google =[1075,-539.5]

mailsecurityauthrication541smtp_xpby_google =[1077,-540.5]

mailsecurityauthrication542smtp_xpby_google =[1079,-541.5]

mailsecurityauthrication543smtp_xpby_google =[1081,-542.5]

mailsecurityauthrication544smtp_xpby_google =[1083,-543.5]

mailsecurityauthrication545smtp_xpby_google =[1085,-544.5]

mailsecurityauthrication546smtp_xpby_google =[1087,-545.5]

mailsecurityauthrication547smtp_xpby_google =[1089,-546.5]

mailsecurityauthrication548smtp_xpby_google =[1091,-547.5]

mailsecurityauthrication549smtp_xpby_google =[1093,-548.5]

mailsecurityauthrication550smtp_xpby_google =[1095,-549.5]

mailsecurityauthrication551smtp_xpby_google =[1097,-550.5]

mailsecurityauthrication552smtp_xpby_google =[1099,-551.5]

mailsecurityauthrication553smtp_xpby_google =[1101,-552.5]

mailsecurityauthrication554smtp_xpby_google =[1103,-553.5]

mailsecurityauthrication555smtp_xpby_google =[1105,-554.5]

mailsecurityauthrication556smtp_xpby_google =[1107,-555.5]

mailsecurityauthrication557smtp_xpby_google =[1109,-556.5]

mailsecurityauthrication558smtp_xpby_google =[1111,-557.5]

mailsecurityauthrication559smtp_xpby_google =[1113,-558.5]

mailsecurityauthrication560smtp_xpby_google =[1115,-559.5]

mailsecurityauthrication561smtp_xpby_google =[1117,-560.5]

mailsecurityauthrication562smtp_xpby_google =[1119,-561.5]

mailsecurityauthrication563smtp_xpby_google =[1121,-562.5]

mailsecurityauthrication564smtp_xpby_google =[1123,-563.5]

mailsecurityauthrication565smtp_xpby_google =[1125,-564.5]

mailsecurityauthrication566smtp_xpby_google =[1127,-565.5]

mailsecurityauthrication567smtp_xpby_google =[1129,-566.5]

mailsecurityauthrication568smtp_xpby_google =[1131,-567.5]

mailsecurityauthrication569smtp_xpby_google =[1133,-568.5]

mailsecurityauthrication570smtp_xpby_google =[1135,-569.5]

mailsecurityauthrication571smtp_xpby_google =[1137,-570.5]

mailsecurityauthrication572smtp_xpby_google =[1139,-571.5]

mailsecurityauthrication573smtp_xpby_google =[1141,-572.5]

mailsecurityauthrication574smtp_xpby_google =[1143,-573.5]

mailsecurityauthrication575smtp_xpby_google =[1145,-574.5]

mailsecurityauthrication576smtp_xpby_google =[1147,-575.5]

mailsecurityauthrication577smtp_xpby_google =[1149,-576.5]

mailsecurityauthrication578smtp_xpby_google =[1151,-577.5]

mailsecurityauthrication579smtp_xpby_google =[1153,-578.5]

mailsecurityauthrication580smtp_xpby_google =[1155,-579.5]

mailsecurityauthrication581smtp_xpby_google =[1157,-580.5]

mailsecurityauthrication582smtp_xpby_google =[1159,-581.5]

mailsecurityauthrication583smtp_xpby_google =[1161,-582.5]

mailsecurityauthrication584smtp_xpby_google =[1163,-583.5]

mailsecurityauthrication585smtp_xpby_google =[1165,-584.5]

mailsecurityauthrication586smtp_xpby_google =[1167,-585.5]

mailsecurityauthrication587smtp_xpby_google =[1169,-586.5]

mailsecurityauthrication588smtp_xpby_google =[1171,-587.5]

mailsecurityauthrication589smtp_xpby_google =[1173,-588.5]

mailsecurityauthrication590smtp_xpby_google =[1175,-589.5]

mailsecurityauthrication591smtp_xpby_google =[1177,-590.5]

mailsecurityauthrication592smtp_xpby_google =[1179,-591.5]

mailsecurityauthrication593smtp_xpby_google =[1181,-592.5]

mailsecurityauthrication594smtp_xpby_google =[1183,-593.5]

mailsecurityauthrication595smtp_xpby_google =[1185,-594.5]

mailsecurityauthrication596smtp_xpby_google =[1187,-595.5]

mailsecurityauthrication597smtp_xpby_google =[1189,-596.5]

mailsecurityauthrication598smtp_xpby_google =[1191,-597.5]

mailsecurityauthrication599smtp_xpby_google =[1193,-598.5]

mailsecurityauthrication600smtp_xpby_google =[1195,-599.5]

mailsecurityauthrication601smtp_xpby_google =[1197,-600.5]

mailsecurityauthrication602smtp_xpby_google =[1199,-601.5]

mailsecurityauthrication603smtp_xpby_google =[1201,-602.5]

mailsecurityauthrication604smtp_xpby_google =[1203,-603.5]

mailsecurityauthrication605smtp_xpby_google =[1205,-604.5]

mailsecurityauthrication606smtp_xpby_google =[1207,-605.5]

mailsecurityauthrication607smtp_xpby_google =[1209,-606.5]

mailsecurityauthrication608smtp_xpby_google =[1211,-607.5]

mailsecurityauthrication609smtp_xpby_google =[1213,-608.5]

mailsecurityauthrication610smtp_xpby_google =[1215,-609.5]

mailsecurityauthrication611smtp_xpby_google =[1217,-610.5]

mailsecurityauthrication612smtp_xpby_google =[1219,-611.5]

mailsecurityauthrication613smtp_xpby_google =[1221,-612.5]

mailsecurityauthrication614smtp_xpby_google =[1223,-613.5]

mailsecurityauthrication615smtp_xpby_google =[1225,-614.5]

mailsecurityauthrication616smtp_xpby_google =[1227,-615.5]

mailsecurityauthrication617smtp_xpby_google =[1229,-616.5]

mailsecurityauthrication618smtp_xpby_google =[1231,-617.5]

mailsecurityauthrication619smtp_xpby_google =[1233,-618.5]

mailsecurityauthrication620smtp_xpby_google =[1235,-619.5]

mailsecurityauthrication621smtp_xpby_google =[1237,-620.5]

mailsecurityauthrication622smtp_xpby_google =[1239,-621.5]

mailsecurityauthrication623smtp_xpby_google =[1241,-622.5]

mailsecurityauthrication624smtp_xpby_google =[1243,-623.5]

mailsecurityauthrication625smtp_xpby_google =[1245,-624.5]

mailsecurityauthrication626smtp_xpby_google =[1247,-625.5]

mailsecurityauthrication627smtp_xpby_google =[1249,-626.5]

mailsecurityauthrication628smtp_xpby_google =[1251,-627.5]

mailsecurityauthrication629smtp_xpby_google =[1253,-628.5]

mailsecurityauthrication630smtp_xpby_google =[1255,-629.5]

mailsecurityauthrication631smtp_xpby_google =[1257,-630.5]

mailsecurityauthrication632smtp_xpby_google =[1259,-631.5]

mailsecurityauthrication633smtp_xpby_google =[1261,-632.5]

mailsecurityauthrication634smtp_xpby_google =[1263,-633.5]

mailsecurityauthrication635smtp_xpby_google =[1265,-634.5]

mailsecurityauthrication636smtp_xpby_google =[1267,-635.5]

mailsecurityauthrication637smtp_xpby_google =[1269,-636.5]

mailsecurityauthrication638smtp_xpby_google =[1271,-637.5]

mailsecurityauthrication639smtp_xpby_google =[1273,-638.5]

mailsecurityauthrication640smtp_xpby_google =[1275,-639.5]

mailsecurityauthrication641smtp_xpby_google =[1277,-640.5]

mailsecurityauthrication642smtp_xpby_google =[1279,-641.5]

mailsecurityauthrication643smtp_xpby_google =[1281,-642.5]

mailsecurityauthrication644smtp_xpby_google =[1283,-643.5]

mailsecurityauthrication645smtp_xpby_google =[1285,-644.5]

mailsecurityauthrication646smtp_xpby_google =[1287,-645.5]

mailsecurityauthrication647smtp_xpby_google =[1289,-646.5]

mailsecurityauthrication648smtp_xpby_google =[1291,-647.5]

mailsecurityauthrication649smtp_xpby_google =[1293,-648.5]

mailsecurityauthrication650smtp_xpby_google =[1295,-649.5]

mailsecurityauthrication651smtp_xpby_google =[1297,-650.5]

mailsecurityauthrication652smtp_xpby_google =[1299,-651.5]

mailsecurityauthrication653smtp_xpby_google =[1301,-652.5]

mailsecurityauthrication654smtp_xpby_google =[1303,-653.5]

mailsecurityauthrication655smtp_xpby_google =[1305,-654.5]

mailsecurityauthrication656smtp_xpby_google =[1307,-655.5]

mailsecurityauthrication657smtp_xpby_google =[1309,-656.5]

mailsecurityauthrication658smtp_xpby_google =[1311,-657.5]

mailsecurityauthrication659smtp_xpby_google =[1313,-658.5]

mailsecurityauthrication660smtp_xpby_google =[1315,-659.5]

mailsecurityauthrication661smtp_xpby_google =[1317,-660.5]

mailsecurityauthrication662smtp_xpby_google =[1319,-661.5]

mailsecurityauthrication663smtp_xpby_google =[1321,-662.5]

mailsecurityauthrication664smtp_xpby_google =[1323,-663.5]

mailsecurityauthrication665smtp_xpby_google =[1325,-664.5]

mailsecurityauthrication666smtp_xpby_google =[1327,-665.5]

mailsecurityauthrication667smtp_xpby_google =[1329,-666.5]

mailsecurityauthrication668smtp_xpby_google =[1331,-667.5]

mailsecurityauthrication669smtp_xpby_google =[1333,-668.5]

mailsecurityauthrication670smtp_xpby_google =[1335,-669.5]

mailsecurityauthrication671smtp_xpby_google =[1337,-670.5]

mailsecurityauthrication672smtp_xpby_google =[1339,-671.5]

mailsecurityauthrication673smtp_xpby_google =[1341,-672.5]

mailsecurityauthrication674smtp_xpby_google =[1343,-673.5]

mailsecurityauthrication675smtp_xpby_google =[1345,-674.5]

mailsecurityauthrication676smtp_xpby_google =[1347,-675.5]

mailsecurityauthrication677smtp_xpby_google =[1349,-676.5]

mailsecurityauthrication678smtp_xpby_google =[1351,-677.5]

mailsecurityauthrication679smtp_xpby_google =[1353,-678.5]

mailsecurityauthrication680smtp_xpby_google =[1355,-679.5]

mailsecurityauthrication681smtp_xpby_google =[1357,-680.5]

mailsecurityauthrication682smtp_xpby_google =[1359,-681.5]

mailsecurityauthrication683smtp_xpby_google =[1361,-682.5]

mailsecurityauthrication684smtp_xpby_google =[1363,-683.5]

mailsecurityauthrication685smtp_xpby_google =[1365,-684.5]

mailsecurityauthrication686smtp_xpby_google =[1367,-685.5]

mailsecurityauthrication687smtp_xpby_google =[1369,-686.5]

mailsecurityauthrication688smtp_xpby_google =[1371,-687.5]

mailsecurityauthrication689smtp_xpby_google =[1373,-688.5]

mailsecurityauthrication690smtp_xpby_google =[1375,-689.5]

mailsecurityauthrication691smtp_xpby_google =[1377,-690.5]

mailsecurityauthrication692smtp_xpby_google =[1379,-691.5]

mailsecurityauthrication693smtp_xpby_google =[1381,-692.5]

mailsecurityauthrication694smtp_xpby_google =[1383,-693.5]

mailsecurityauthrication695smtp_xpby_google =[1385,-694.5]

mailsecurityauthrication696smtp_xpby_google =[1387,-695.5]

mailsecurityauthrication697smtp_xpby_google =[1389,-696.5]

mailsecurityauthrication698smtp_xpby_google =[1391,-697.5]

mailsecurityauthrication699smtp_xpby_google =[1393,-698.5]

mailsecurityauthrication700smtp_xpby_google =[1395,-699.5]

mailsecurityauthrication701smtp_xpby_google =[1397,-700.5]

mailsecurityauthrication702smtp_xpby_google =[1399,-701.5]

mailsecurityauthrication703smtp_xpby_google =[1401,-702.5]

mailsecurityauthrication704smtp_xpby_google =[1403,-703.5]

mailsecurityauthrication705smtp_xpby_google =[1405,-704.5]

mailsecurityauthrication706smtp_xpby_google =[1407,-705.5]

mailsecurityauthrication707smtp_xpby_google =[1409,-706.5]

mailsecurityauthrication708smtp_xpby_google =[1411,-707.5]

mailsecurityauthrication709smtp_xpby_google =[1413,-708.5]

mailsecurityauthrication710smtp_xpby_google =[1415,-709.5]

mailsecurityauthrication711smtp_xpby_google =[1417,-710.5]

mailsecurityauthrication712smtp_xpby_google =[1419,-711.5]

mailsecurityauthrication713smtp_xpby_google =[1421,-712.5]

mailsecurityauthrication714smtp_xpby_google =[1423,-713.5]

mailsecurityauthrication715smtp_xpby_google =[1425,-714.5]

mailsecurityauthrication716smtp_xpby_google =[1427,-715.5]

mailsecurityauthrication717smtp_xpby_google =[1429,-716.5]

mailsecurityauthrication718smtp_xpby_google =[1431,-717.5]

mailsecurityauthrication719smtp_xpby_google =[1433,-718.5]

mailsecurityauthrication720smtp_xpby_google =[1435,-719.5]

mailsecurityauthrication721smtp_xpby_google =[1437,-720.5]

mailsecurityauthrication722smtp_xpby_google =[1439,-721.5]

mailsecurityauthrication723smtp_xpby_google =[1441,-722.5]

mailsecurityauthrication724smtp_xpby_google =[1443,-723.5]

mailsecurityauthrication725smtp_xpby_google =[1445,-724.5]

mailsecurityauthrication726smtp_xpby_google =[1447,-725.5]

mailsecurityauthrication727smtp_xpby_google =[1449,-726.5]

mailsecurityauthrication728smtp_xpby_google =[1451,-727.5]

mailsecurityauthrication729smtp_xpby_google =[1453,-728.5]

mailsecurityauthrication730smtp_xpby_google =[1455,-729.5]

mailsecurityauthrication731smtp_xpby_google =[1457,-730.5]

mailsecurityauthrication732smtp_xpby_google =[1459,-731.5]

mailsecurityauthrication733smtp_xpby_google =[1461,-732.5]

mailsecurityauthrication734smtp_xpby_google =[1463,-733.5]

mailsecurityauthrication735smtp_xpby_google =[1465,-734.5]

mailsecurityauthrication736smtp_xpby_google =[1467,-735.5]

mailsecurityauthrication737smtp_xpby_google =[1469,-736.5]

mailsecurityauthrication738smtp_xpby_google =[1471,-737.5]

mailsecurityauthrication739smtp_xpby_google =[1473,-738.5]

mailsecurityauthrication740smtp_xpby_google =[1475,-739.5]

mailsecurityauthrication741smtp_xpby_google =[1477,-740.5]

mailsecurityauthrication742smtp_xpby_google =[1479,-741.5]

mailsecurityauthrication743smtp_xpby_google =[1481,-742.5]

mailsecurityauthrication744smtp_xpby_google =[1483,-743.5]

mailsecurityauthrication745smtp_xpby_google =[1485,-744.5]

mailsecurityauthrication746smtp_xpby_google =[1487,-745.5]

mailsecurityauthrication747smtp_xpby_google =[1489,-746.5]

mailsecurityauthrication748smtp_xpby_google =[1491,-747.5]

mailsecurityauthrication749smtp_xpby_google =[1493,-748.5]

mailsecurityauthrication750smtp_xpby_google =[1495,-749.5]

mailsecurityauthrication751smtp_xpby_google =[1497,-750.5]

mailsecurityauthrication752smtp_xpby_google =[1499,-751.5]

mailsecurityauthrication753smtp_xpby_google =[1501,-752.5]

mailsecurityauthrication754smtp_xpby_google =[1503,-753.5]

mailsecurityauthrication755smtp_xpby_google =[1505,-754.5]

mailsecurityauthrication756smtp_xpby_google =[1507,-755.5]

mailsecurityauthrication757smtp_xpby_google =[1509,-756.5]

mailsecurityauthrication758smtp_xpby_google =[1511,-757.5]

mailsecurityauthrication759smtp_xpby_google =[1513,-758.5]

mailsecurityauthrication760smtp_xpby_google =[1515,-759.5]

mailsecurityauthrication761smtp_xpby_google =[1517,-760.5]

mailsecurityauthrication762smtp_xpby_google =[1519,-761.5]

mailsecurityauthrication763smtp_xpby_google =[1521,-762.5]

mailsecurityauthrication764smtp_xpby_google =[1523,-763.5]

mailsecurityauthrication765smtp_xpby_google =[1525,-764.5]

mailsecurityauthrication766smtp_xpby_google =[1527,-765.5]

mailsecurityauthrication767smtp_xpby_google =[1529,-766.5]

mailsecurityauthrication768smtp_xpby_google =[1531,-767.5]

mailsecurityauthrication769smtp_xpby_google =[1533,-768.5]

mailsecurityauthrication770smtp_xpby_google =[1535,-769.5]

mailsecurityauthrication771smtp_xpby_google =[1537,-770.5]

mailsecurityauthrication772smtp_xpby_google =[1539,-771.5]

mailsecurityauthrication773smtp_xpby_google =[1541,-772.5]

mailsecurityauthrication774smtp_xpby_google =[1543,-773.5]

mailsecurityauthrication775smtp_xpby_google =[1545,-774.5]

mailsecurityauthrication776smtp_xpby_google =[1547,-775.5]

mailsecurityauthrication777smtp_xpby_google =[1549,-776.5]

mailsecurityauthrication778smtp_xpby_google =[1551,-777.5]

mailsecurityauthrication779smtp_xpby_google =[1553,-778.5]

mailsecurityauthrication780smtp_xpby_google =[1555,-779.5]

mailsecurityauthrication781smtp_xpby_google =[1557,-780.5]

mailsecurityauthrication782smtp_xpby_google =[1559,-781.5]

mailsecurityauthrication783smtp_xpby_google =[1561,-782.5]

mailsecurityauthrication784smtp_xpby_google =[1563,-783.5]

mailsecurityauthrication785smtp_xpby_google =[1565,-784.5]

mailsecurityauthrication786smtp_xpby_google =[1567,-785.5]

mailsecurityauthrication787smtp_xpby_google =[1569,-786.5]

mailsecurityauthrication788smtp_xpby_google =[1571,-787.5]

mailsecurityauthrication789smtp_xpby_google =[1573,-788.5]

mailsecurityauthrication790smtp_xpby_google =[1575,-789.5]

mailsecurityauthrication791smtp_xpby_google =[1577,-790.5]

mailsecurityauthrication792smtp_xpby_google =[1579,-791.5]

mailsecurityauthrication793smtp_xpby_google =[1581,-792.5]

mailsecurityauthrication794smtp_xpby_google =[1583,-793.5]

mailsecurityauthrication795smtp_xpby_google =[1585,-794.5]

mailsecurityauthrication796smtp_xpby_google =[1587,-795.5]

mailsecurityauthrication797smtp_xpby_google =[1589,-796.5]

mailsecurityauthrication798smtp_xpby_google =[1591,-797.5]

mailsecurityauthrication799smtp_xpby_google =[1593,-798.5]

mailsecurityauthrication800smtp_xpby_google =[1595,-799.5]

mailsecurityauthrication801smtp_xpby_google =[1597,-800.5]

mailsecurityauthrication802smtp_xpby_google =[1599,-801.5]

mailsecurityauthrication803smtp_xpby_google =[1601,-802.5]

mailsecurityauthrication804smtp_xpby_google =[1603,-803.5]

mailsecurityauthrication805smtp_xpby_google =[1605,-804.5]

mailsecurityauthrication806smtp_xpby_google =[1607,-805.5]

mailsecurityauthrication807smtp_xpby_google =[1609,-806.5]

mailsecurityauthrication808smtp_xpby_google =[1611,-807.5]

mailsecurityauthrication809smtp_xpby_google =[1613,-808.5]

mailsecurityauthrication810smtp_xpby_google =[1615,-809.5]

mailsecurityauthrication811smtp_xpby_google =[1617,-810.5]

mailsecurityauthrication812smtp_xpby_google =[1619,-811.5]

mailsecurityauthrication813smtp_xpby_google =[1621,-812.5]

mailsecurityauthrication814smtp_xpby_google =[1623,-813.5]

mailsecurityauthrication815smtp_xpby_google =[1625,-814.5]

mailsecurityauthrication816smtp_xpby_google =[1627,-815.5]

mailsecurityauthrication817smtp_xpby_google =[1629,-816.5]

mailsecurityauthrication818smtp_xpby_google =[1631,-817.5]

mailsecurityauthrication819smtp_xpby_google =[1633,-818.5]

mailsecurityauthrication820smtp_xpby_google =[1635,-819.5]

mailsecurityauthrication821smtp_xpby_google =[1637,-820.5]

mailsecurityauthrication822smtp_xpby_google =[1639,-821.5]

mailsecurityauthrication823smtp_xpby_google =[1641,-822.5]

mailsecurityauthrication824smtp_xpby_google =[1643,-823.5]

mailsecurityauthrication825smtp_xpby_google =[1645,-824.5]

mailsecurityauthrication826smtp_xpby_google =[1647,-825.5]

mailsecurityauthrication827smtp_xpby_google =[1649,-826.5]

mailsecurityauthrication828smtp_xpby_google =[1651,-827.5]

mailsecurityauthrication829smtp_xpby_google =[1653,-828.5]

mailsecurityauthrication830smtp_xpby_google =[1655,-829.5]

mailsecurityauthrication831smtp_xpby_google =[1657,-830.5]

mailsecurityauthrication832smtp_xpby_google =[1659,-831.5]

mailsecurityauthrication833smtp_xpby_google =[1661,-832.5]

mailsecurityauthrication834smtp_xpby_google =[1663,-833.5]

mailsecurityauthrication835smtp_xpby_google =[1665,-834.5]

mailsecurityauthrication836smtp_xpby_google =[1667,-835.5]

mailsecurityauthrication837smtp_xpby_google =[1669,-836.5]

mailsecurityauthrication838smtp_xpby_google =[1671,-837.5]

mailsecurityauthrication839smtp_xpby_google =[1673,-838.5]

mailsecurityauthrication840smtp_xpby_google =[1675,-839.5]

mailsecurityauthrication841smtp_xpby_google =[1677,-840.5]

mailsecurityauthrication842smtp_xpby_google =[1679,-841.5]

mailsecurityauthrication843smtp_xpby_google =[1681,-842.5]

mailsecurityauthrication844smtp_xpby_google =[1683,-843.5]

mailsecurityauthrication845smtp_xpby_google =[1685,-844.5]

mailsecurityauthrication846smtp_xpby_google =[1687,-845.5]

mailsecurityauthrication847smtp_xpby_google =[1689,-846.5]

mailsecurityauthrication848smtp_xpby_google =[1691,-847.5]

mailsecurityauthrication849smtp_xpby_google =[1693,-848.5]

mailsecurityauthrication850smtp_xpby_google =[1695,-849.5]

mailsecurityauthrication851smtp_xpby_google =[1697,-850.5]

mailsecurityauthrication852smtp_xpby_google =[1699,-851.5]

mailsecurityauthrication853smtp_xpby_google =[1701,-852.5]

mailsecurityauthrication854smtp_xpby_google =[1703,-853.5]

mailsecurityauthrication855smtp_xpby_google =[1705,-854.5]

mailsecurityauthrication856smtp_xpby_google =[1707,-855.5]

mailsecurityauthrication857smtp_xpby_google =[1709,-856.5]

mailsecurityauthrication858smtp_xpby_google =[1711,-857.5]

mailsecurityauthrication859smtp_xpby_google =[1713,-858.5]

mailsecurityauthrication860smtp_xpby_google =[1715,-859.5]

mailsecurityauthrication861smtp_xpby_google =[1717,-860.5]

mailsecurityauthrication862smtp_xpby_google =[1719,-861.5]

mailsecurityauthrication863smtp_xpby_google =[1721,-862.5]

mailsecurityauthrication864smtp_xpby_google =[1723,-863.5]

mailsecurityauthrication865smtp_xpby_google =[1725,-864.5]

mailsecurityauthrication866smtp_xpby_google =[1727,-865.5]

mailsecurityauthrication867smtp_xpby_google =[1729,-866.5]

mailsecurityauthrication868smtp_xpby_google =[1731,-867.5]

mailsecurityauthrication869smtp_xpby_google =[1733,-868.5]

mailsecurityauthrication870smtp_xpby_google =[1735,-869.5]

mailsecurityauthrication871smtp_xpby_google =[1737,-870.5]

mailsecurityauthrication872smtp_xpby_google =[1739,-871.5]

mailsecurityauthrication873smtp_xpby_google =[1741,-872.5]

mailsecurityauthrication874smtp_xpby_google =[1743,-873.5]

mailsecurityauthrication875smtp_xpby_google =[1745,-874.5]

mailsecurityauthrication876smtp_xpby_google =[1747,-875.5]

mailsecurityauthrication877smtp_xpby_google =[1749,-876.5]

mailsecurityauthrication878smtp_xpby_google =[1751,-877.5]

mailsecurityauthrication879smtp_xpby_google =[1753,-878.5]

mailsecurityauthrication880smtp_xpby_google =[1755,-879.5]

mailsecurityauthrication881smtp_xpby_google =[1757,-880.5]

mailsecurityauthrication882smtp_xpby_google =[1759,-881.5]

mailsecurityauthrication883smtp_xpby_google =[1761,-882.5]

mailsecurityauthrication884smtp_xpby_google =[1763,-883.5]

mailsecurityauthrication885smtp_xpby_google =[1765,-884.5]

mailsecurityauthrication886smtp_xpby_google =[1767,-885.5]

mailsecurityauthrication887smtp_xpby_google =[1769,-886.5]

mailsecurityauthrication888smtp_xpby_google =[1771,-887.5]

mailsecurityauthrication889smtp_xpby_google =[1773,-888.5]

mailsecurityauthrication890smtp_xpby_google =[1775,-889.5]

mailsecurityauthrication891smtp_xpby_google =[1777,-890.5]

mailsecurityauthrication892smtp_xpby_google =[1779,-891.5]

mailsecurityauthrication893smtp_xpby_google =[1781,-892.5]

mailsecurityauthrication894smtp_xpby_google =[1783,-893.5]

mailsecurityauthrication895smtp_xpby_google =[1785,-894.5]

mailsecurityauthrication896smtp_xpby_google =[1787,-895.5]

mailsecurityauthrication897smtp_xpby_google =[1789,-896.5]

mailsecurityauthrication898smtp_xpby_google =[1791,-897.5]

mailsecurityauthrication899smtp_xpby_google =[1793,-898.5]

mailsecurityauthrication900smtp_xpby_google =[1795,-899.5]

mailsecurityauthrication901smtp_xpby_google =[1797,-900.5]

mailsecurityauthrication902smtp_xpby_google =[1799,-901.5]

mailsecurityauthrication903smtp_xpby_google =[1801,-902.5]

mailsecurityauthrication904smtp_xpby_google =[1803,-903.5]

mailsecurityauthrication905smtp_xpby_google =[1805,-904.5]

mailsecurityauthrication906smtp_xpby_google =[1807,-905.5]

mailsecurityauthrication907smtp_xpby_google =[1809,-906.5]

mailsecurityauthrication908smtp_xpby_google =[1811,-907.5]

mailsecurityauthrication909smtp_xpby_google =[1813,-908.5]

mailsecurityauthrication910smtp_xpby_google =[1815,-909.5]

mailsecurityauthrication911smtp_xpby_google =[1817,-910.5]

mailsecurityauthrication912smtp_xpby_google =[1819,-911.5]

mailsecurityauthrication913smtp_xpby_google =[1821,-912.5]

mailsecurityauthrication914smtp_xpby_google =[1823,-913.5]

mailsecurityauthrication915smtp_xpby_google =[1825,-914.5]

mailsecurityauthrication916smtp_xpby_google =[1827,-915.5]

mailsecurityauthrication917smtp_xpby_google =[1829,-916.5]

mailsecurityauthrication918smtp_xpby_google =[1831,-917.5]

mailsecurityauthrication919smtp_xpby_google =[1833,-918.5]

mailsecurityauthrication920smtp_xpby_google =[1835,-919.5]

mailsecurityauthrication921smtp_xpby_google =[1837,-920.5]

mailsecurityauthrication922smtp_xpby_google =[1839,-921.5]

mailsecurityauthrication923smtp_xpby_google =[1841,-922.5]

mailsecurityauthrication924smtp_xpby_google =[1843,-923.5]

mailsecurityauthrication925smtp_xpby_google =[1845,-924.5]

mailsecurityauthrication926smtp_xpby_google =[1847,-925.5]

mailsecurityauthrication927smtp_xpby_google =[1849,-926.5]

mailsecurityauthrication928smtp_xpby_google =[1851,-927.5]

mailsecurityauthrication929smtp_xpby_google =[1853,-928.5]

mailsecurityauthrication930smtp_xpby_google =[1855,-929.5]

mailsecurityauthrication931smtp_xpby_google =[1857,-930.5]

mailsecurityauthrication932smtp_xpby_google =[1859,-931.5]

mailsecurityauthrication933smtp_xpby_google =[1861,-932.5]

mailsecurityauthrication934smtp_xpby_google =[1863,-933.5]

mailsecurityauthrication935smtp_xpby_google =[1865,-934.5]

mailsecurityauthrication936smtp_xpby_google =[1867,-935.5]

mailsecurityauthrication937smtp_xpby_google =[1869,-936.5]

mailsecurityauthrication938smtp_xpby_google =[1871,-937.5]

mailsecurityauthrication939smtp_xpby_google =[1873,-938.5]

mailsecurityauthrication940smtp_xpby_google =[1875,-939.5]

mailsecurityauthrication941smtp_xpby_google =[1877,-940.5]

mailsecurityauthrication942smtp_xpby_google =[1879,-941.5]

mailsecurityauthrication943smtp_xpby_google =[1881,-942.5]

mailsecurityauthrication944smtp_xpby_google =[1883,-943.5]

mailsecurityauthrication945smtp_xpby_google =[1885,-944.5]

mailsecurityauthrication946smtp_xpby_google =[1887,-945.5]

mailsecurityauthrication947smtp_xpby_google =[1889,-946.5]

mailsecurityauthrication948smtp_xpby_google =[1891,-947.5]

mailsecurityauthrication949smtp_xpby_google =[1893,-948.5]

mailsecurityauthrication950smtp_xpby_google =[1895,-949.5]

mailsecurityauthrication951smtp_xpby_google =[1897,-950.5]

mailsecurityauthrication952smtp_xpby_google =[1899,-951.5]

mailsecurityauthrication953smtp_xpby_google =[1901,-952.5]

mailsecurityauthrication954smtp_xpby_google =[1903,-953.5]

mailsecurityauthrication955smtp_xpby_google =[1905,-954.5]

mailsecurityauthrication956smtp_xpby_google =[1907,-955.5]

mailsecurityauthrication957smtp_xpby_google =[1909,-956.5]

mailsecurityauthrication958smtp_xpby_google =[1911,-957.5]

mailsecurityauthrication959smtp_xpby_google =[1913,-958.5]

mailsecurityauthrication960smtp_xpby_google =[1915,-959.5]

mailsecurityauthrication961smtp_xpby_google =[1917,-960.5]

mailsecurityauthrication962smtp_xpby_google =[1919,-961.5]

mailsecurityauthrication963smtp_xpby_google =[1921,-962.5]

mailsecurityauthrication964smtp_xpby_google =[1923,-963.5]

mailsecurityauthrication965smtp_xpby_google =[1925,-964.5]

mailsecurityauthrication966smtp_xpby_google =[1927,-965.5]

mailsecurityauthrication967smtp_xpby_google =[1929,-966.5]

mailsecurityauthrication968smtp_xpby_google =[1931,-967.5]

mailsecurityauthrication969smtp_xpby_google =[1933,-968.5]

mailsecurityauthrication970smtp_xpby_google =[1935,-969.5]

mailsecurityauthrication971smtp_xpby_google =[1937,-970.5]

mailsecurityauthrication972smtp_xpby_google =[1939,-971.5]

mailsecurityauthrication973smtp_xpby_google =[1941,-972.5]

mailsecurityauthrication974smtp_xpby_google =[1943,-973.5]

mailsecurityauthrication975smtp_xpby_google =[1945,-974.5]

mailsecurityauthrication976smtp_xpby_google =[1947,-975.5]

mailsecurityauthrication977smtp_xpby_google =[1949,-976.5]

mailsecurityauthrication978smtp_xpby_google =[1951,-977.5]

mailsecurityauthrication979smtp_xpby_google =[1953,-978.5]

mailsecurityauthrication980smtp_xpby_google =[1955,-979.5]

mailsecurityauthrication981smtp_xpby_google =[1957,-980.5]

mailsecurityauthrication982smtp_xpby_google =[1959,-981.5]

mailsecurityauthrication983smtp_xpby_google =[1961,-982.5]

mailsecurityauthrication984smtp_xpby_google =[1963,-983.5]

mailsecurityauthrication985smtp_xpby_google =[1965,-984.5]

mailsecurityauthrication986smtp_xpby_google =[1967,-985.5]

mailsecurityauthrication987smtp_xpby_google =[1969,-986.5]

mailsecurityauthrication988smtp_xpby_google =[1971,-987.5]

mailsecurityauthrication989smtp_xpby_google =[1973,-988.5]

mailsecurityauthrication990smtp_xpby_google =[1975,-989.5]

mailsecurityauthrication991smtp_xpby_google =[1977,-990.5]

mailsecurityauthrication992smtp_xpby_google =[1979,-991.5]

mailsecurityauthrication993smtp_xpby_google =[1981,-992.5]

mailsecurityauthrication994smtp_xpby_google =[1983,-993.5]

mailsecurityauthrication995smtp_xpby_google =[1985,-994.5]

mailsecurityauthrication996smtp_xpby_google =[1987,-995.5]

mailsecurityauthrication997smtp_xpby_google =[1989,-996.5]

mailsecurityauthrication998smtp_xpby_google =[1991,-997.5]

mailsecurityauthrication999smtp_xpby_google =[1993,-998.5]



def loading_animation():
    animation = "|/-\\"
    for i in range(10):  
        time.sleep(0.2) 
        sys.stdout.write("\r" + "Sending " + animation[i % len(animation)])
        sys.stdout.flush()
    input()
    sys.stdout.write("\n")
    print("Sending complete!")


def clear():
    if os.name == "posix":
        os.system('clear')
    if os.name == "nt":
        os.system("cls")


# For the complicity of code
yellow = Fore.YELLOW
green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
white = Fore.WHITE
magenta = Fore.MAGENTA
colour = ["yellow", "green", "cyan", "magenta"]

current_time = time.strftime("%H:%M:%S")


def ct():
    print("Current time:", current_time)


def logo():
    a = " _____  __        __   _     __  __       _ _"
    b = "|_   _| \ \      / /__| |__ |  \/  | __ _(_) |"
    c = "  | |____\ \ /\ / / _ \ '_ \| |\/| |/ _` | | |"
    d = "  | |_____\ V  V /  __/ |_) | |  | | (_| | | |"
    e = "  |_|      \_/\_/ \___|_.__/|_|  |_|\__,_|_|_|"
    f = "===================================================="
    a1 = yellow + a
    b1 = red + b
    c1 = cyan + c
    d1 = green + d
    e1 = magenta + e
    f1 = cyan + f
    print(f1)
    print(a1)
    time.sleep(0.3)
    print(b1)
    time.sleep(0.3)
    print(c1)
    time.sleep(0.3)
    print(d1)
    time.sleep(0.3)
    print(e1)
    time.sleep(0.3)
    print(f1)


logo()


def colour_of_ran():
    ah = lucky.randint(1, 8)
    if ah == 1:
        x = Fore.YELLOW
        return x
    elif ah == 2:
        x = Fore.GREEN
        return x
    elif ah == 3:
        x = Fore.CYAN
        return x
    elif ah == 4:
        x = Fore.MAGENTA
        return x
    elif ah == 5:
        x = Fore.LIGHTCYAN_EX
        return x
    elif ah == 6:
        x = Fore.LIGHTBLUE_EX
        return x
    elif ah == 7:
        x = Fore.LIGHTGREEN_EX
        return x
    elif ah == 8:
        x = Fore.LIGHTMAGENTA_EX
        return x
    else:
        c = Fore.GREEN
        return c


def get_ip_addressed():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        ip_address = sock.getsockname()[0]
    finally:
        # Close the socket
        sock.close()
    return ip_address


# Call the function to get the IP address


def check_smtp_login(smtp_host, smtp_port, username, password):
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            login_result = server.login(username, password)

            if login_result[0] == 235:
                print("SMTP login successful")
                return 2
            else:
                print("SMTP login failed")
                return 4
    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication failed")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def send_emails(x, y, sender_email, sender_password, receiver_email, subject, message):
    # Create the email message
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = ",".join(receiver_email)
    email['Subject'] = subject

    # Attach the message to the email
    email.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(x, y)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(email)

    # Disconnect from the server
    server.quit()


def add(a):
    list_mails.append(a)
    print("Entered...")


def main():
    ask1c = colour_of_ran()
    ask1 = ask1c + "Enter your server address : "
    ask2c = colour_of_ran()
    ask2 = ask2c + "Enter your server's port (587 recommended) *only numbers : "
    ask3c = colour_of_ran()
    ask3 = ask3c + "Enter your EMAIL-ID : "
    ask4c = colour_of_ran()
    ask4 = ask4c + "Enter your EMAIL-ID's password : "
    quesN = input(ask1)
    try:
        quesP = int(input(ask2))
    except:
        print(
            "Only Number allowed...\nPlease, try again...\nGood bye ,,, \nIf you wanted to our software then be careful and run the programme again... ")
        time.sleep(2)
        clear()
        sys.exit(1)
    quesE = input(ask3)
    quesEP = input(ask4)
    ip_add = get_ip_addressed()

    log_in = check_smtp_login(quesN, quesP, quesE, quesEP)
    if log_in == 2:
        ct()
        print(f"Your IP-Address if {ip_add}")

        sa2 = colour_of_ran()
        say2 = sa2 + "Enter subject : "
        sa3 = colour_of_ran()
        say3 = sa3 + "Enter body of The mail : "
        subject = input(say2)
        body = input(say3)

        sa1 = colour_of_ran()
        say1 = sa1 + "Enter receiver's Email-id (Write done to complete) :"
        while True:
            email_adder = input(say1)
            if email_adder == "done":
                break
            else:
                list_mails.append(email_adder)

        demo_mail = f"\n\n\nFrom : {quesE}\n---------------\nTo : {list_mails}\n-----------------\n{subject} \n-------------------------\n{body}"
        send_emails(quesN, quesP, quesE, quesEP, list_mails, subject, body)
        print(demo_mail)
        ct()
        loading_animation()


main()
