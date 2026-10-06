"""Page copy for the Porta privacy policy and support page, per language.

Placeholders in braces ({publisher}, {address}, {email}, {updated}) are filled
from site.json by build.py. Everything else is the published text: edit it
here, then run `python3 tools/build.py`.

The facts in the privacy policy were checked against the Porta app
(repo orocoro/04xPorj, Guichet/): no accounts, an empty privacy manifest,
no analytics SDK, location resolved once on device (LocationStore.swift),
and network hosts limited to the services listed under "connections".
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
    "links": "ch.ch, alertswiss.ch",
    "photos": "myswitzerland.com, schweizmobil.ch, stnet.ch",
}

PRIVACY = {
    "en": [
        ("Who is responsible", "<p>{publisher}, {address}. Contact: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Short version", "<p>Porta has no accounts, no analytics, no advertising and no tracking. The app does not collect personal data, and we run no server that receives data from the app.</p>"),
        ("Location", "<p>If you tap “Find the commune at your current location”, the app asks iOS for your location once, works out the commune on your device and uses it only to show that commune. Your location is not stored and is not sent to us or anyone else. You can refuse or withdraw location access at any time in the iOS Settings.</p>"),
        ("What stays on your device", "<p>Favorites, recent searches and your chosen home commune are stored only on your device, in an app group shared with Porta’s own widgets. Nothing is uploaded. Deleting the app deletes this data.</p>"),
        ("Connections the app makes", "<p>To show content, the app contacts these public services directly from your device. They can see your IP address and handle it under their own privacy policies:</p><ul>"
            "<li>Federal Statistical Office ({bfs}): commune data.</li>"
            "<li>MeteoAlarm ({meteo}): weather warnings on the emergency card.</li>"
            "<li>{links} and official commune and portal websites: only when you open a link.</li>"
            "<li>Switzerland Tourism and partners ({photos}): photos in Discover.</li></ul>"),
        ("If you contact us", "<p>If you write to us by e-mail, we use your address and message only to answer you, and delete them when they are no longer needed for that.</p>"),
        ("This website", "<p>This page is hosted on GitHub Pages. GitHub may log your IP address when you visit it, under the <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>. The page uses no cookies and no tracking.</p>"),
        ("Children", "<p>The app is not directed at children and collects no data from anyone.</p>"),
        ("Your rights", "<p>Under the Swiss Federal Act on Data Protection (FADP) and, where it applies, the GDPR, you can ask what data we hold about you and have it corrected or deleted. Because the app collects no personal data, this only concerns e-mails you send us. Write to <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Changes", "<p>If the app ever starts handling data differently, we will update this page before the change ships.</p>"),
    ],
    "de": [
        ("Verantwortlich", "<p>{publisher}, {address}. Kontakt: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Kurzfassung", "<p>Porta hat keine Konten, keine Analyse, keine Werbung und kein Tracking. Die App erhebt keine Personendaten, und wir betreiben keinen Server, der Daten aus der App empfängt.</p>"),
        ("Standort", "<p>Wenn Sie «Gemeinde am aktuellen Standort ermitteln» antippen, fragt die App iOS einmalig nach Ihrem Standort, ermittelt die Gemeinde auf Ihrem Gerät und verwendet sie nur, um diese Gemeinde anzuzeigen. Der Standort wird weder gespeichert noch an uns oder Dritte übermittelt. Sie können den Zugriff jederzeit in den iOS-Einstellungen verweigern oder widerrufen.</p>"),
        ("Was auf Ihrem Gerät bleibt", "<p>Favoriten, letzte Suchen und Ihre Wohngemeinde werden nur auf Ihrem Gerät gespeichert, in einer App-Gruppe, die nur die Widgets von Porta nutzen. Es wird nichts hochgeladen. Wenn Sie die App löschen, werden diese Daten gelöscht.</p>"),
        ("Verbindungen der App", "<p>Um Inhalte anzuzeigen, ruft die App diese öffentlichen Dienste direkt von Ihrem Gerät ab. Diese sehen dabei Ihre IP-Adresse und bearbeiten sie gemäss ihren eigenen Datenschutzbestimmungen:</p><ul>"
            "<li>Bundesamt für Statistik ({bfs}): Gemeindedaten.</li>"
            "<li>MeteoAlarm ({meteo}): Wetterwarnungen auf der Notruf-Karte.</li>"
            "<li>{links} sowie offizielle Gemeinde- und Portalseiten: nur, wenn Sie einen Link öffnen.</li>"
            "<li>Schweiz Tourismus und Partner ({photos}): Fotos in Discover.</li></ul>"),
        ("Wenn Sie uns schreiben", "<p>Wenn Sie uns per E-Mail kontaktieren, verwenden wir Ihre Adresse und Nachricht nur, um Ihnen zu antworten, und löschen sie, sobald sie dafür nicht mehr nötig sind.</p>"),
        ("Diese Website", "<p>Diese Seite wird über GitHub Pages bereitgestellt. GitHub kann beim Aufruf Ihre IP-Adresse protokollieren, gemäss dem <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>. Die Seite verwendet keine Cookies und kein Tracking.</p>"),
        ("Kinder", "<p>Die App richtet sich nicht an Kinder und erhebt von niemandem Daten.</p>"),
        ("Ihre Rechte", "<p>Nach dem Datenschutzgesetz (DSG) und, soweit anwendbar, der DSGVO können Sie Auskunft über Ihre Daten verlangen und deren Berichtigung oder Löschung beantragen. Da die App keine Personendaten erhebt, betrifft das nur E-Mails, die Sie uns senden. Schreiben Sie an <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Änderungen", "<p>Sollte die App Daten künftig anders bearbeiten, passen wir diese Seite an, bevor die Änderung erscheint.</p>"),
    ],
    "fr": [
        ("Responsable", "<p>{publisher}, {address}. Contact : <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("En bref", "<p>Porta n’a ni comptes, ni outils d’analyse, ni publicité, ni pistage. L’app ne collecte aucune donnée personnelle et nous n’exploitons aucun serveur qui reçoit des données de l’app.</p>"),
        ("Localisation", "<p>Si vous touchez « Déterminer la commune du lieu actuel », l’app demande une seule fois votre position à iOS, détermine la commune sur votre appareil et l’utilise uniquement pour afficher cette commune. Votre position n’est ni enregistrée ni transmise à nous ou à des tiers. Vous pouvez refuser ou retirer l’accès à tout moment dans les réglages d’iOS.</p>"),
        ("Ce qui reste sur votre appareil", "<p>Les favoris, les recherches récentes et votre commune de domicile sont enregistrés uniquement sur votre appareil, dans un groupe d’apps partagé avec les widgets de Porta. Rien n’est téléversé. Supprimer l’app supprime ces données.</p>"),
        ("Connexions de l’app", "<p>Pour afficher du contenu, l’app contacte directement depuis votre appareil les services publics suivants. Ils voient votre adresse IP et la traitent selon leur propre politique de confidentialité :</p><ul>"
            "<li>Office fédéral de la statistique ({bfs}) : données des communes.</li>"
            "<li>MeteoAlarm ({meteo}) : alertes météo sur la carte d’urgence.</li>"
            "<li>{links} et sites officiels des communes et portails : uniquement lorsque vous ouvrez un lien.</li>"
            "<li>Suisse Tourisme et partenaires ({photos}) : photos dans Discover.</li></ul>"),
        ("Si vous nous écrivez", "<p>Si vous nous contactez par e-mail, nous utilisons votre adresse et votre message uniquement pour vous répondre et les supprimons dès qu’ils ne sont plus nécessaires à cette fin.</p>"),
        ("Ce site", "<p>Cette page est hébergée sur GitHub Pages. GitHub peut enregistrer votre adresse IP lors de votre visite, selon la <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>. La page n’utilise ni cookies ni pistage.</p>"),
        ("Enfants", "<p>L’app ne s’adresse pas aux enfants et ne collecte aucune donnée, de personne.</p>"),
        ("Vos droits", "<p>Selon la loi fédérale sur la protection des données (LPD) et, le cas échéant, le RGPD, vous pouvez demander quelles données nous détenons sur vous et les faire rectifier ou effacer. Comme l’app ne collecte aucune donnée personnelle, cela ne concerne que les e-mails que vous nous envoyez. Écrivez à <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("Modifications", "<p>Si l’app devait un jour traiter des données autrement, nous mettrons cette page à jour avant la publication du changement.</p>"),
    ],
    "it": [
        ("Responsabile", "<p>{publisher}, {address}. Contatto: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ("In breve", "<p>Porta non ha account, analisi, pubblicità né tracciamento. L’app non raccoglie dati personali e non gestiamo alcun server che riceva dati dall’app.</p>"),
        ("Posizione", "<p>Se toccate «Determinare il comune del luogo attuale», l’app chiede a iOS la vostra posizione una sola volta, individua il comune sul vostro dispositivo e la usa solo per mostrare quel comune. La posizione non viene salvata né trasmessa a noi o a terzi. Potete negare o revocare l’accesso in qualsiasi momento nelle Impostazioni di iOS.</p>"),
        ("Cosa resta sul vostro dispositivo", "<p>Preferiti, ricerche recenti e il vostro comune di domicilio sono salvati solo sul vostro dispositivo, in un gruppo di app condiviso con i widget di Porta. Nulla viene caricato. Eliminando l’app, questi dati vengono eliminati.</p>"),
        ("Connessioni dell’app", "<p>Per mostrare i contenuti, l’app contatta direttamente dal vostro dispositivo i seguenti servizi pubblici. Questi vedono il vostro indirizzo IP e lo trattano secondo le proprie informative sulla privacy:</p><ul>"
            "<li>Ufficio federale di statistica ({bfs}): dati dei comuni.</li>"
            "<li>MeteoAlarm ({meteo}): allerte meteo sulla scheda emergenze.</li>"
            "<li>{links} e siti ufficiali di comuni e portali: solo quando aprite un link.</li>"
            "<li>Svizzera Turismo e partner ({photos}): foto in Discover.</li></ul>"),
        ("Se ci scrivete", "<p>Se ci contattate via e-mail, usiamo il vostro indirizzo e il messaggio solo per rispondervi e li eliminiamo quando non servono più a tale scopo.</p>"),
        ("Questo sito", "<p>Questa pagina è ospitata su GitHub Pages. GitHub può registrare il vostro indirizzo IP durante la visita, secondo il <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>. La pagina non usa cookie né tracciamento.</p>"),
        ("Bambini", "<p>L’app non è rivolta ai bambini e non raccoglie dati da nessuno.</p>"),
        ("I vostri diritti", "<p>Secondo la legge federale sulla protezione dei dati (LPD) e, se applicabile, il GDPR, potete chiedere quali dati abbiamo su di voi e chiederne la rettifica o la cancellazione. Poiché l’app non raccoglie dati personali, ciò riguarda solo le e-mail che ci inviate. Scrivete a <a href=\"mailto:{email}\">{email}</a>.</p>"),
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
