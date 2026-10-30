"""Page copy for the Porta privacy policy and support page, per language.

Placeholders in braces ({publisher}, {address}, {email}, {updated}) are filled
from site.json by build.py. Everything else is the published text: edit it
here, then run `python3 tools/build.py`.

The facts in the privacy policy were checked against the Porta app
(repo orocoro/04xPorj, Guichet/): no accounts, an empty privacy manifest,
no analytics SDK, location requested once and only its commune looked up (LocationStore.swift),
and network hosts limited to the services listed under "connections"
(rechecked 2026-10-17: the commune lookup now sends one coordinate to
api3.geo.admin.ch, falling back to Apple's CLGeocoder).
"""

LANGS = ["en", "de", "fr", "it"]

LANG_NAMES = {"en": "English", "de": "Deutsch", "fr": "Français", "it": "Italiano"}

UI = {
    "en": {
        "privacy": "Privacy Policy",
        "support": "Support",
        "updated": "Last updated",
        "home_intro": "Porta is an independent iPhone and iPad app that helps you find Swiss public information and the authority responsible for it, in German, French, Italian, Romansh and English.",
        "not_official": "Porta is not an official service of the Swiss Confederation, the cantons or the communes.",
        "language": "Language",
    },
    "de": {
        "privacy": "Datenschutzerklärung",
        "support": "Support",
        "updated": "Zuletzt aktualisiert",
        "home_intro": "Porta ist eine unabhängige App für iPhone und iPad. Sie hilft Ihnen, öffentliche Informationen der Schweiz und die zuständige Stelle zu finden, auf Deutsch, Französisch, Italienisch, Rätoromanisch und Englisch.",
        "not_official": "Porta ist kein offizielles Angebot des Bundes, der Kantone oder der Gemeinden.",
        "language": "Sprache",
    },
    "fr": {
        "privacy": "Politique de confidentialité",
        "support": "Assistance",
        "updated": "Dernière mise à jour",
        "home_intro": "Porta est une app indépendante pour iPhone et iPad. Elle vous aide à trouver les informations publiques suisses et l’autorité compétente, en allemand, français, italien, romanche et anglais.",
        "not_official": "Porta n’est pas un service officiel de la Confédération, des cantons ou des communes.",
        "language": "Langue",
    },
    "it": {
        "privacy": "Informativa sulla privacy",
        "support": "Assistenza",
        "updated": "Ultimo aggiornamento",
        "home_intro": "Porta è un’app indipendente per iPhone e iPad. Vi aiuta a trovare le informazioni pubbliche svizzere e l’autorità competente, in tedesco, francese, italiano, romancio e inglese.",
        "not_official": "Porta non è un servizio ufficiale della Confederazione, dei cantoni o dei comuni.",
        "language": "Lingua",
    },
}

# Hosts the app contacts. Kept in one place so every language lists the same set.
HOSTS = {
    "bfs": "agvchapp.bfs.admin.ch",
    "meteo": "feeds.meteoalarm.org",
    "geo": "api3.geo.admin.ch",
    "links": "ch.ch, alertswiss.ch",
    "photos": "myswitzerland.com, schweizmobil.ch, stnet.ch",
    "tiles": "wmts.geo.admin.ch",
    "weather": "data.geo.admin.ch",
    "votes": "ogd-static.voteinfo-app.ch",
    "slf": "aws.slf.ch",
    "news": "www.newsd.admin.ch",
    "cantons": "www.ai.ch, www.api.news.apps.be.ch, www.fr.ch, www.ge.ch, www.gr.ch, www.jura.ch, www.ne.ch, daten.sg.ch, www.tg.ch, www.ur.ch, www.vd.ch",
}

PRIVACY = {
    "en": [
        ("Who is responsible", "<p>{publisher}, {address}. Contact: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Short version", "<p>Porta has no accounts, no analytics, no advertising and no tracking. The app does not collect personal data, and we run no server that receives data from the app.</p>"),
        ("Location", "<p>If you tap “Find the commune at your current location”, the app asks iOS for your location once. To find the commune, it sends that one coordinate to the official commune-boundary service of the Federal Office of Topography swisstopo ({geo}); if that gives no answer, iOS’s own geocoder (Apple) is asked instead. Neither request contains anything else about you. The app uses the result only to show that commune and does not store your location; we never receive it. You can refuse or withdraw location access at any time in the iOS Settings.</p>"),
        ("What stays on your device", "<p>Favorites, recent searches and your chosen home commune are stored only on your device, in an app group shared with Porta’s own widgets. Nothing is uploaded. Deleting the app deletes this data.</p>"),
        ("Connections the app makes", "<p>To show content, the app contacts these public services directly from your device. They can see your IP address and handle it under their own privacy policies:</p><ul>"
            "<li>Federal Statistical Office ({bfs}): commune data.</li>"
            "<li>MeteoAlarm ({meteo}): weather warnings on the emergency card.</li>"
            "<li>Federal Office of Topography swisstopo ({tiles}): national map tiles when a map is shown. The request reveals the map area being shown, not your location. Tiles already loaded stay in the app’s cache on your device.</li>"
            "<li>MeteoSwiss ({weather}): weather forecasts on the commune page.</li>"
            "<li>Federal Statistical Office ({votes}): results of federal votes.</li>"
            "<li>WSL Institute for Snow and Avalanche Research SLF ({slf}): the avalanche bulletin in winter.</li>"
            "<li>These three files each cover all of Switzerland, so the request does not reveal which commune you look at.</li>"
            "<li>Federal Chancellery, News Service Bund ({news}): the latest federal press releases under “News &amp; Media”. The list is the same for all of Switzerland.</li>"
            "<li>Your home canton, if it publishes its press releases as a feed ({cantons}): its latest press releases on “My commune”. The canton sees that someone loads its press releases, but not which commune you chose.</li>"
            "<li>{links} and other official federal, cantonal and commune websites: only when you open a link.</li>"
            "<li>Switzerland Tourism and partners ({photos}): photos in Discover.</li></ul>"),
        ("If you contact us", "<p>If you write to us by e-mail, we use your address and message only to answer you, and delete them when they are no longer needed for that.</p>"),
        ("This website", "<p>This page is hosted on GitHub Pages by GitHub, Inc. in the United States. GitHub may log your IP address when you visit it, under the <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>; this can mean your IP address is processed abroad. The page uses no cookies and no tracking. E-mails to us are handled by Proton AG in Switzerland.</p>"),
        ("Children", "<p>The app is not directed at children and collects no data from anyone.</p>"),
        ("Your rights and applicable law", "<p>This policy is governed by Swiss law, in particular the Federal Act on Data Protection (FADP). You can ask what data we hold about you and have it corrected or deleted. Because the app collects no personal data, this only concerns e-mails you send us. Write to <a href=\"mailto:{email}\">{email}</a>. You can also complain to the <a href=\"https://www.edoeb.admin.ch\">Federal Data Protection and Information Commissioner (FDPIC)</a>.</p>"),
        ("Changes", "<p>If the app ever starts handling data differently, we will update this page before the change ships.</p>"),
    ],
    "de": [
        ("Verantwortlich", "<p>{publisher}, {address}. Kontakt: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Kurzfassung", "<p>Porta hat keine Konten, keine Analyse, keine Werbung und kein Tracking. Die App erhebt keine Personendaten, und wir betreiben keinen Server, der Daten aus der App empfängt.</p>"),
        ("Standort", "<p>Wenn Sie «Gemeinde am aktuellen Standort ermitteln» antippen, fragt die App iOS einmalig nach Ihrem Standort. Um die Gemeinde zu bestimmen, sendet sie diese eine Koordinate an den offiziellen Gemeindegrenzen-Dienst des Bundesamts für Landestopografie swisstopo ({geo}); liefert er keine Antwort, wird stattdessen der Geocoder von iOS (Apple) gefragt. Keine der Anfragen enthält weitere Angaben über Sie. Die App verwendet das Ergebnis nur, um diese Gemeinde anzuzeigen, und speichert den Standort nicht; wir erhalten ihn nie. Sie können den Zugriff jederzeit in den iOS-Einstellungen verweigern oder widerrufen.</p>"),
        ("Was auf Ihrem Gerät bleibt", "<p>Favoriten, letzte Suchen und Ihre Wohngemeinde werden nur auf Ihrem Gerät gespeichert, in einer App-Gruppe, die nur die Widgets von Porta nutzen. Es wird nichts hochgeladen. Wenn Sie die App löschen, werden diese Daten gelöscht.</p>"),
        ("Verbindungen der App", "<p>Um Inhalte anzuzeigen, ruft die App diese öffentlichen Dienste direkt von Ihrem Gerät ab. Diese sehen dabei Ihre IP-Adresse und bearbeiten sie gemäss ihren eigenen Datenschutzbestimmungen:</p><ul>"
            "<li>Bundesamt für Statistik ({bfs}): Gemeindedaten.</li>"
            "<li>MeteoAlarm ({meteo}): Wetterwarnungen auf der Notruf-Karte.</li>"
            "<li>Bundesamt für Landestopografie swisstopo ({tiles}): Kartenausschnitte der Landeskarte, wenn eine Karte angezeigt wird. Dabei wird der gezeigte Kartenausschnitt übermittelt, nicht Ihr Standort. Bereits geladene Ausschnitte bleiben im Zwischenspeicher der App auf Ihrem Gerät.</li>"
            "<li>MeteoSchweiz ({weather}): Wetterprognosen auf der Gemeindeseite.</li>"
            "<li>Bundesamt für Statistik ({votes}): Resultate eidgenössischer Abstimmungen.</li>"
            "<li>WSL-Institut für Schnee- und Lawinenforschung SLF ({slf}): im Winter das Lawinenbulletin.</li>"
            "<li>Diese drei Dateien gelten jeweils für die ganze Schweiz; die Anfrage verrät also nicht, welche Gemeinde Sie ansehen.</li>"
            "<li>Schweizerische Bundeskanzlei, News Service Bund ({news}): die neusten Medienmitteilungen des Bundes unter «News &amp; Medien». Die Liste ist für die ganze Schweiz dieselbe.</li>"
            "<li>Ihr Wohnkanton, wenn er seine Medienmitteilungen als Feed veröffentlicht ({cantons}): seine neusten Medienmitteilungen auf «Meine Gemeinde». Der Kanton sieht dabei, dass jemand seine Mitteilungen lädt, aber nicht, welche Gemeinde Sie gewählt haben.</li>"
            "<li>{links} sowie weitere offizielle Seiten von Bund, Kantonen und Gemeinden: nur, wenn Sie einen Link öffnen.</li>"
            "<li>Schweiz Tourismus und Partner ({photos}): Fotos in Discover.</li></ul>"),
        ("Wenn Sie uns schreiben", "<p>Wenn Sie uns per E-Mail kontaktieren, verwenden wir Ihre Adresse und Nachricht nur, um Ihnen zu antworten, und löschen sie, sobald sie dafür nicht mehr nötig sind.</p>"),
        ("Diese Website", "<p>Diese Seite wird über GitHub Pages von GitHub, Inc. in den USA bereitgestellt. GitHub kann beim Aufruf Ihre IP-Adresse protokollieren, gemäss dem <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>; Ihre IP-Adresse kann dabei im Ausland bearbeitet werden. Die Seite verwendet keine Cookies und kein Tracking. E-Mails an uns laufen über Proton AG in der Schweiz.</p>"),
        ("Kinder", "<p>Die App richtet sich nicht an Kinder und erhebt von niemandem Daten.</p>"),
        ("Ihre Rechte und anwendbares Recht", "<p>Diese Erklärung untersteht Schweizer Recht, insbesondere dem Bundesgesetz über den Datenschutz (DSG). Sie können Auskunft über Ihre Daten verlangen und deren Berichtigung oder Löschung beantragen. Da die App keine Personendaten erhebt, betrifft das nur E-Mails, die Sie uns senden. Schreiben Sie an <a href=\"mailto:{email}\">{email}</a>. Sie können sich auch an den <a href=\"https://www.edoeb.admin.ch\">Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB)</a> wenden.</p>"),
        ("Änderungen", "<p>Sollte die App Daten künftig anders bearbeiten, passen wir diese Seite an, bevor die Änderung erscheint.</p>"),
    ],
    "fr": [
        ("Responsable", "<p>{publisher}, {address}. Contact : <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("En bref", "<p>Porta n’a ni comptes, ni outils d’analyse, ni publicité, ni pistage. L’app ne collecte aucune donnée personnelle et nous n’exploitons aucun serveur qui reçoit des données de l’app.</p>"),
        ("Localisation", "<p>Si vous touchez « Déterminer la commune du lieu actuel », l’app demande une seule fois votre position à iOS. Pour trouver la commune, elle envoie cette seule coordonnée au service officiel des limites communales de l’Office fédéral de topographie swisstopo ({geo}) ; s’il ne répond pas, le géocodeur d’iOS (Apple) est interrogé à la place. Aucune de ces requêtes ne contient d’autre information sur vous. L’app utilise le résultat uniquement pour afficher cette commune et n’enregistre pas votre position ; nous ne la recevons jamais. Vous pouvez refuser ou retirer l’accès à tout moment dans les réglages d’iOS.</p>"),
        ("Ce qui reste sur votre appareil", "<p>Les favoris, les recherches récentes et votre commune de domicile sont enregistrés uniquement sur votre appareil, dans un groupe d’apps partagé avec les widgets de Porta. Rien n’est téléversé. Supprimer l’app supprime ces données.</p>"),
        ("Connexions de l’app", "<p>Pour afficher du contenu, l’app contacte directement depuis votre appareil les services publics suivants. Ils voient votre adresse IP et la traitent selon leur propre politique de confidentialité :</p><ul>"
            "<li>Office fédéral de la statistique ({bfs}) : données des communes.</li>"
            "<li>MeteoAlarm ({meteo}) : alertes météo sur la carte d’urgence.</li>"
            "<li>Office fédéral de topographie swisstopo ({tiles}) : tuiles de la carte nationale lorsqu’une carte est affichée. La requête indique la zone affichée, pas votre position. Les tuiles déjà chargées restent dans le cache de l’app sur votre appareil.</li>"
            "<li>MétéoSuisse ({weather}) : prévisions météo sur la page de la commune.</li>"
            "<li>Office fédéral de la statistique ({votes}) : résultats des votations fédérales.</li>"
            "<li>WSL Institut pour l’étude de la neige et des avalanches SLF ({slf}) : le bulletin d’avalanches en hiver.</li>"
            "<li>Ces trois fichiers couvrent chacun toute la Suisse ; la requête ne révèle donc pas quelle commune vous consultez.</li>"
            "<li>Chancellerie fédérale, News Service Bund ({news}) : les derniers communiqués de presse de la Confédération sous « Actualités &amp; médias ». La liste est la même pour toute la Suisse.</li>"
            "<li>Votre canton de domicile, s’il publie ses communiqués sous forme de flux ({cantons}) : ses derniers communiqués sous « Ma commune ». Le canton voit alors que quelqu’un charge ses communiqués, mais pas quelle commune vous avez choisie.</li>"
            "<li>{links} et autres sites officiels de la Confédération, des cantons et des communes : uniquement lorsque vous ouvrez un lien.</li>"
            "<li>Suisse Tourisme et partenaires ({photos}) : photos dans Discover.</li></ul>"),
        ("Si vous nous écrivez", "<p>Si vous nous contactez par e-mail, nous utilisons votre adresse et votre message uniquement pour vous répondre et les supprimons dès qu’ils ne sont plus nécessaires à cette fin.</p>"),
        ("Ce site", "<p>Cette page est hébergée sur GitHub Pages par GitHub, Inc. aux États-Unis. GitHub peut enregistrer votre adresse IP lors de votre visite, selon la <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a> ; votre adresse IP peut ainsi être traitée à l’étranger. La page n’utilise ni cookies ni pistage. Les e-mails qui nous sont adressés transitent par Proton AG, en Suisse.</p>"),
        ("Enfants", "<p>L’app ne s’adresse pas aux enfants et ne collecte aucune donnée, de personne.</p>"),
        ("Vos droits et droit applicable", "<p>Cette politique est régie par le droit suisse, en particulier la loi fédérale sur la protection des données (LPD). Vous pouvez demander quelles données nous détenons sur vous et les faire rectifier ou effacer. Comme l’app ne collecte aucune donnée personnelle, cela ne concerne que les e-mails que vous nous envoyez. Écrivez à <a href=\"mailto:{email}\">{email}</a>. Vous pouvez aussi vous adresser au <a href=\"https://www.edoeb.admin.ch\">Préposé fédéral à la protection des données et à la transparence (PFPDT)</a>.</p>"),
        ("Modifications", "<p>Si l’app devait un jour traiter des données autrement, nous mettrons cette page à jour avant la publication du changement.</p>"),
    ],
    "it": [
        ("Responsabile", "<p>{publisher}, {address}. Contatto: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("In breve", "<p>Porta non ha account, analisi, pubblicità né tracciamento. L’app non raccoglie dati personali e non gestiamo alcun server che riceva dati dall’app.</p>"),
        ("Posizione", "<p>Se toccate «Determinare il comune del luogo attuale», l’app chiede a iOS la vostra posizione una sola volta. Per trovare il comune invia quest’unica coordinata al servizio ufficiale dei confini comunali dell’Ufficio federale di topografia swisstopo ({geo}); se non risponde, viene interpellato il geocodificatore di iOS (Apple). Nessuna di queste richieste contiene altri dati su di voi. L’app usa il risultato solo per mostrare quel comune e non salva la posizione; noi non la riceviamo mai. Potete negare o revocare l’accesso in qualsiasi momento nelle Impostazioni di iOS.</p>"),
        ("Cosa resta sul vostro dispositivo", "<p>Preferiti, ricerche recenti e il vostro comune di domicilio sono salvati solo sul vostro dispositivo, in un gruppo di app condiviso con i widget di Porta. Nulla viene caricato. Eliminando l’app, questi dati vengono eliminati.</p>"),
        ("Connessioni dell’app", "<p>Per mostrare i contenuti, l’app contatta direttamente dal vostro dispositivo i seguenti servizi pubblici. Questi vedono il vostro indirizzo IP e lo trattano secondo le proprie informative sulla privacy:</p><ul>"
            "<li>Ufficio federale di statistica ({bfs}): dati dei comuni.</li>"
            "<li>MeteoAlarm ({meteo}): allerte meteo sulla scheda emergenze.</li>"
            "<li>Ufficio federale di topografia swisstopo ({tiles}): tasselli della carta nazionale quando viene mostrata una mappa. La richiesta indica la zona mostrata, non la vostra posizione. I tasselli già caricati restano nella cache dell’app sul vostro dispositivo.</li>"
            "<li>MeteoSvizzera ({weather}): previsioni meteo sulla pagina del comune.</li>"
            "<li>Ufficio federale di statistica ({votes}): risultati delle votazioni federali.</li>"
            "<li>Istituto WSL per lo studio della neve e delle valanghe SLF ({slf}): il bollettino delle valanghe in inverno.</li>"
            "<li>Questi tre file coprono ciascuno tutta la Svizzera; la richiesta non rivela quindi quale comune state consultando.</li>"
            "<li>Cancelleria federale, News Service Bund ({news}): gli ultimi comunicati stampa della Confederazione in «Notizie &amp; media». L’elenco è lo stesso per tutta la Svizzera.</li>"
            "<li>Il vostro Cantone di domicilio, se pubblica i suoi comunicati come feed ({cantons}): i suoi ultimi comunicati in «Il mio comune». Il Cantone vede così che qualcuno carica i suoi comunicati, ma non quale comune avete scelto.</li>"
            "<li>{links} e altri siti ufficiali di Confederazione, cantoni e comuni: solo quando aprite un link.</li>"
            "<li>Svizzera Turismo e partner ({photos}): foto in Discover.</li></ul>"),
        ("Se ci scrivete", "<p>Se ci contattate via e-mail, usiamo il vostro indirizzo e il messaggio solo per rispondervi e li eliminiamo quando non servono più a tale scopo.</p>"),
        ("Questo sito", "<p>Questa pagina è ospitata su GitHub Pages da GitHub, Inc. negli Stati Uniti. GitHub può registrare il vostro indirizzo IP durante la visita, secondo il <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>; il vostro indirizzo IP può quindi essere trattato all’estero. La pagina non usa cookie né tracciamento. Le e-mail che ci inviate passano per Proton AG, in Svizzera.</p>"),
        ("Bambini", "<p>L’app non è rivolta ai bambini e non raccoglie dati da nessuno.</p>"),
        ("I vostri diritti e diritto applicabile", "<p>La presente informativa è disciplinata dal diritto svizzero, in particolare dalla legge federale sulla protezione dei dati (LPD). Potete chiedere quali dati abbiamo su di voi e chiederne la rettifica o la cancellazione. Poiché l’app non raccoglie dati personali, ciò riguarda solo le e-mail che ci inviate. Scrivete a <a href=\"mailto:{email}\">{email}</a>. Potete anche rivolgervi all’<a href=\"https://www.edoeb.admin.ch\">Incaricato federale della protezione dei dati e della trasparenza (IFPDT)</a>.</p>"),
        ("Modifiche", "<p>Se in futuro l’app dovesse trattare i dati in modo diverso, aggiorneremo questa pagina prima che la modifica venga pubblicata.</p>"),
    ],
}

SUPPORT = {
    "en": [
        ("Contact", "<p>Write to <a href=\"mailto:{email}\">{email}</a>. Please include your device, iOS version and, if it is about an entry, its name.</p>"),
        ("Common questions", "<dl>"
            "<dt>A commune website link is missing.</dt><dd>Links are verified automatically, and a commune without a verified website shows no link. Send us the address and we will add it.</dd>"
            "<dt>Some information is wrong or out of date.</dt><dd>Tell us the entry and what is wrong. We correct the data source or the entry.</dd>"
            "<dt>Do I need an account or an internet connection?</dt><dd>No account. The Discover catalog works offline; commune data, weather warnings and photos need a connection.</dd>"
            "<dt>Is my location stored?</dt><dd>No. See the <a href=\"privacy.html\">privacy policy</a>.</dd></dl>"),
        ("Data sources and credits", "<ul>"
            "<li>Commune data: © Federal Statistical Office (BFS), Neuchâtel.</li>"
            "<li>Discover content: Switzerland Tourism open data (CC BY-SA). The source and a backlink are shown on each entry; photos belong to their owners.</li>"
            "<li>Editorial photos: Wikimedia Commons, with license and author shown on each photo.</li></ul>"),
    ],
    "de": [
        ("Kontakt", "<p>Schreiben Sie an <a href=\"mailto:{email}\">{email}</a>. Nennen Sie bitte Ihr Gerät, die iOS-Version und, falls es um einen Eintrag geht, dessen Namen.</p>"),
        ("Häufige Fragen", "<dl>"
            "<dt>Der Link zur Gemeinde-Website fehlt.</dt><dd>Links werden automatisch geprüft; eine Gemeinde ohne geprüfte Website zeigt keinen Link. Senden Sie uns die Adresse, und wir ergänzen sie.</dd>"
            "<dt>Eine Angabe ist falsch oder veraltet.</dt><dd>Nennen Sie uns den Eintrag und was nicht stimmt. Wir korrigieren die Datenquelle oder den Eintrag.</dd>"
            "<dt>Brauche ich ein Konto oder Internet?</dt><dd>Kein Konto. Der Discover-Katalog funktioniert offline; Gemeindedaten, Wetterwarnungen und Fotos brauchen eine Verbindung.</dd>"
            "<dt>Wird mein Standort gespeichert?</dt><dd>Nein. Siehe <a href=\"privacy.html\">Datenschutzerklärung</a>.</dd></dl>"),
        ("Datenquellen und Nachweise", "<ul>"
            "<li>Gemeindedaten: © Bundesamt für Statistik (BFS), Neuchâtel.</li>"
            "<li>Discover-Inhalte: Open Data von Schweiz Tourismus (CC BY-SA). Quelle und Backlink stehen bei jedem Eintrag; Fotos gehören ihren Urhebern.</li>"
            "<li>Redaktionelle Fotos: Wikimedia Commons, Lizenz und Urheber stehen bei jedem Foto.</li></ul>"),
    ],
    "fr": [
        ("Contact", "<p>Écrivez à <a href=\"mailto:{email}\">{email}</a>. Indiquez votre appareil, la version d’iOS et, s’il s’agit d’une entrée, son nom.</p>"),
        ("Questions fréquentes", "<dl>"
            "<dt>Le lien vers le site de la commune manque.</dt><dd>Les liens sont vérifiés automatiquement ; une commune sans site vérifié n’affiche aucun lien. Envoyez-nous l’adresse et nous l’ajouterons.</dd>"
            "<dt>Une information est fausse ou dépassée.</dt><dd>Indiquez-nous l’entrée et ce qui ne va pas. Nous corrigeons la source de données ou l’entrée.</dd>"
            "<dt>Faut-il un compte ou une connexion internet ?</dt><dd>Aucun compte. Le catalogue Discover fonctionne hors ligne ; les données des communes, les alertes météo et les photos nécessitent une connexion.</dd>"
            "<dt>Ma position est-elle enregistrée ?</dt><dd>Non. Voir la <a href=\"privacy.html\">politique de confidentialité</a>.</dd></dl>"),
        ("Sources et crédits", "<ul>"
            "<li>Données des communes : © Office fédéral de la statistique (OFS), Neuchâtel.</li>"
            "<li>Contenu Discover : données ouvertes de Suisse Tourisme (CC BY-SA). La source et un lien figurent sur chaque entrée ; les photos appartiennent à leurs auteurs.</li>"
            "<li>Photos éditoriales : Wikimedia Commons, licence et auteur indiqués sur chaque photo.</li></ul>"),
    ],
    "it": [
        ("Contatto", "<p>Scrivete a <a href=\"mailto:{email}\">{email}</a>. Indicate il dispositivo, la versione di iOS e, se riguarda una voce, il suo nome.</p>"),
        ("Domande frequenti", "<dl>"
            "<dt>Manca il link al sito del comune.</dt><dd>I link sono verificati automaticamente; un comune senza sito verificato non mostra alcun link. Inviateci l’indirizzo e lo aggiungeremo.</dd>"
            "<dt>Un’informazione è errata o non aggiornata.</dt><dd>Indicateci la voce e cosa non va. Correggiamo la fonte dei dati o la voce.</dd>"
            "<dt>Serve un account o una connessione internet?</dt><dd>Nessun account. Il catalogo Discover funziona offline; dati dei comuni, allerte meteo e foto richiedono una connessione.</dd>"
            "<dt>La mia posizione viene salvata?</dt><dd>No. Vedete l’<a href=\"privacy.html\">informativa sulla privacy</a>.</dd></dl>"),
        ("Fonti dei dati e crediti", "<ul>"
            "<li>Dati dei comuni: © Ufficio federale di statistica (UST), Neuchâtel.</li>"
            "<li>Contenuti Discover: open data di Svizzera Turismo (CC BY-SA). Fonte e link sono indicati in ogni voce; le foto appartengono ai rispettivi autori.</li>"
            "<li>Foto editoriali: Wikimedia Commons, con licenza e autore indicati su ogni foto.</li></ul>"),
    ],
}
