#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QuickRecon v0.3.2
# Copyright (C) 2011 Filip Szymański <f.szymanski@hotmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
# Please note that this tool was created and published for educational purposes only.
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import ConfigParser
import httplib
import random
import re
import socket
import sys
import urllib2

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

import sip
sip.setapi("QVariant", 2)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_mainwindow import Ui_MainWindow
from ui_xfndialog import Ui_XFNDialog
from ui_aboutdialog import Ui_AboutDialog

import images_rc

database = ["adm", "admin", "admins", "agent", "aix", "alerts", "av", "antivirus", "app", "apps", "appserver",
            "archive", "as400", "auto", "backup", "banking", "bbdd", "bbs", "bea", "beta", "blog", "catalog",
            "cgi", "channel", "channels", "chat", "cisco", "client", "clients", "club", "cluster", "clusters",
            "code", "commerce",	"community", "compaq", "console", "consumer", "contact", "contracts", "corporate",
            "ceo", "cso", "cust", "customer", "data", "bd", "db2", "default", "demo", "design",	"desktop", "dev",
            "develop", "developer", "device", "dial", "digital", "dir",	"directory", "disc", "discovery", "disk",
            "dns", "dns1", "dns2", "dns3", "docs", "documents", "domain", "domains", "dominoweb", "download",
            "downloads", "ecommerce", "e-commerce", "edi", "edu", "education", "email", "enable", "engine",
            "engineer",	"enterprise", "event", "events", "example", "exchange", "extern", "external", "extranet",
            "fax", "field", "finance", "firewall", "forum", "forums", "fsp", "ftp",	"ftp2", "fw", "fw1", "gallery",
            "galleries", "games", "gateway", "gopher", "guest",	"gw", "hello", "helloworld", "help", "helpdesk",
            "helponline", "hp", "ibm", "ibmdb",	"ids", "ILMI", "images", "imap", "imap4", "img", "imgs", "info",
            "intern", "internal", "intranet", "invalid", "iphone", "ipsec", "irc", "ircserver", "jobs", "ldap",
            "link",	"linux", "lists", "listserver", "local", "localhost", "log", "logs", "login", "lotus", "mail",
            "mailboxes", "mailhost", "management", "manage", "manager", "map", "maps", "marketing", "device",
            "media", "member", "members", "messenger", "mngt", "mobile", "monitor", "multimedia", "music", "names",
            "net", "netdata", "netstats", "network", "news", "nms", "nntp", "ns", "ns1", "ns2", "ns3", "ntp",
            "online", "openview", "oracle",	"outlook", "page", "pages", "partner", "partners", "pda", "personal",
            "ph", "pictures", "pix", "pop", "pop3", "portal", "press", "print", "printer", "private", "project",
            "projects", "proxy", "public", "ra", "radio", "raptor", "ras", "read", "register", "remote", "report",
            "reports", "root", "router", "rwhois", "sac", "schedules", "scotty", "search", "secret", "secure",
            "security", "seri", "serv", "serv2", "server", "service", "services", "shop", "shopping", "site", "sms",
            "smtp", "smtphost", "snmp", "snmpd", "snort", "solaris", "solutions", "support", "source", "sql", "ssl",
            "stats", "store", "stream", "streaming", "sun", "support", "switch", "sysback", "system", "tech",
            "terminal", "test", "testing", "testing123", "time", "tivoli", "training", "transfers",	"uddi",
            "update", "upload", "uploads", "video", "vpn", "w1", "w2", "w3", "wais", "wap",	"web", "webdocs",
            "weblib", "weblogic", "webmail", "webserver", "webservices", "websphere", "whois", "wireless", "work",
            "world", "write", "ws", "ws1", "ws2", "ws3", "www1", "www2", "www3", "error", "cpanel", "my"]

agents = ["Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
          "Opera/9.80 (Windows NT 5.1; U; pl) Presto/2.8.131 Version/11.10",
          "Links (2.3pre1; Linux 2.6.38-8-generic i686; 160x40)",
          "Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
          "Lynx/2.8.8dev.7 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.8.6",
          "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24",
          "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
          "Mozilla/5.0 (compatible; Konqueror/4.6; Linux) KHTML/4.6.0 (like Gecko) SUSE",
          "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20101005 Fedora/3.6.10-1.fc14 Firefox/3.6.10",
          "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)"]

xfn = ["friend", "acquaintance", "contact", "met", "co-worker", "colleague",
       "co-resident", "neighbor", "child", "parent", "sibling", "spouse",
       "kin", "muse", "crush", "date", "sweetheart", "me"]

license = ("This program is free software: you can redistribute it and/or modify "
           "it under the terms of the GNU General Public License as published by "
           "the Free Software Foundation, either version 3 of the License, or "
           "(at your option) any later version.<p/>"
           "<p>This program is distributed in the hope that it will be useful, "
           "but WITHOUT ANY WARRANTY; without even the implied warranty of "
           "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the "
           "GNU General Public License for more details.<p/>"
           "<p>You should have received a copy of the GNU General Public License "
           "along with this program. If not, see <a href='http://www.gnu.org/licenses/'>"
           "http://www.gnu.org/licenses/</a>.")

info = QString.fromUtf8("QuickRecon ver. 0.3.2"
                        "<p>A simple information gathering utility, based on Qt4 toolkit."
                        "<p>Copyright (C) 2011 Filip Szymański"
                        "<p>E-mail: f.szymanski@hotmail.com"
                        "<p>Home page: <a href='http://code.google.com/p/quickrecon/'>"
                        "http://quickrecon.googlecode.com</a>")

class XFNDialog(QDialog, Ui_XFNDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)

        self.setupUi(self)

        self.connect(self.buttonBox, SIGNAL("accepted()"), SLOT("accept()"))

class AboutDialog(QDialog, Ui_AboutDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)

        self.setupUi(self)

        self.label_2.setText(info)

        self.textBrowser.setText(license)

        self.connect(self.buttonBox, SIGNAL("accepted()"), SLOT("accept()"))

class QuickRecon(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.buffer = StringIO()

        self.setupUi(self)

        self.readSettings()

        self.verticalLayout_3.addStretch(1)
        self.verticalLayout_5.addStretch(1)
        self.verticalLayout_6.addStretch(1)
        self.verticalLayout_7.addStretch(1)
        self.verticalLayout_8.addStretch(1)

        self.connect(self.actionSaveAs, SIGNAL("triggered()"), self.saveAs)
        self.connect(self.actionExit, SIGNAL("triggered()"), self.exitApplication)
        self.connect(self.actionXFN, SIGNAL("triggered()"), self.xfnReference)
        self.connect(self.actionAbout, SIGNAL("triggered()"), self.about)

        self.connect(self.pushButton, SIGNAL("clicked()"), self.exitApplication)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.run)
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.selectFile)

    def run(self):
        if self.tabWidget.currentIndex() == 0:
            if self.lineEdit.text():
                self.findSubdomains()
        elif self.tabWidget.currentIndex() == 1:
            if self.lineEdit_3.text():
                self.findEmails()
        elif self.tabWidget.currentIndex() == 2:
            if self.lineEdit_4.text():
                self.findHumanRelationships()
        elif self.tabWidget.currentIndex() == 3:
            if self.lineEdit_5.text():
                self.zoneTransfer()
        elif self.tabWidget.currentIndex() == 4:
            parser = ConfigParser.SafeConfigParser()
            parser.read("shodan_key.cfg")
            key = parser.get("API key", "key")
            if self.lineEdit_6.text():
                if self.lineEdit_7.text():
                    self.checkShodan(str(self.lineEdit_7.text()))
                elif key:
                    self.checkShodan(key)
                else:
                    QMessageBox.information(self, "Information",
                                            ("You need an API key to access the Shodan database with QuickRecon. "
                                            "Key can be stored in the \'shodan_key.cfg\' file "
                                            "or directly entered in the GUI."))
                    return

    def xfnReference(self):
        dialog = XFNDialog(self)
        dialog.exec_()

    def about(self):
        dialog = AboutDialog(self)
        dialog.exec_()

    def readSettings(self):
        settings = QSettings("quickrecon", "settings")
        position = settings.value("position", QPoint(200, 200))
        self.move(position)

    def writeSettings(self):
        settings = QSettings("quickrecon", "settings")
        settings.setValue("position", self.pos())

    def selectFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Select file")
        if fileName:
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(fileName)

    def saveAs(self):
        fileName = QFileDialog.getSaveFileName(self, "Save as")
        if fileName:
            _file = QFile(fileName)
            if not _file.open(QFile.WriteOnly | QFile.Text):
                QMessageBox.warning(self, "Error",
                                    "Cannot write file %s.\n%s." % (fileName, _file.errorString()))
                return

            stream = QTextStream(_file)
            stream.setCodec("utf8")
            stream << self.textEdit.toPlainText()
            _file.close()

    def checkHost(self, hostname):
        try:
            ip = socket.gethostbyname(hostname)
            self.buffer.write(hostname + " :  " + ip + "\n")
        except:
            pass

    def testWildcard(self):
        results = []
        charset = "abcdefghijklmnopqrstuvwxyz0123456789"
        for count in range(3):
            randomCharset = random.sample(charset, random.randint(6, 12))
            subdomain = "%s.%s" % ("".join(randomCharset), str(self.lineEdit.text()))
            try:
                connection = httplib.HTTPConnection(subdomain)
                connection.putrequest("GET", "/")
                connection.putheader("User-Agent", random.choice(agents))
                connection.endheaders()
                response = connection.getresponse()
                results.append(response.status)
            except:
                pass

        if not results:
            return False
        else:
            return True

    def searchEngine(self):
        urls = []
        if self.checkBox.isChecked():
            for count in range(0, self.spinBox.value(), 10):
                urls.append("http://www.google.com/search?hl=en&ie=UTF-8&num=10&q=%40" +
                            str(self.lineEdit_3.text()) + "&start=" + str(count))

        if self.checkBox_2.isChecked():
            for count in range(0, self.spinBox.value(), 10):
                urls.append("http://groups.google.com/groups?hl=en&ie=UTF-8&num=10&q=%40" +
                            str(self.lineEdit_3.text()) + "&start=" + str(count))

        if self.checkBox_3.isChecked():
            for count in range(1, self.spinBox.value() + 1, 10):
                urls.append("http://www.bing.com/search?q=%40" + str(self.lineEdit_3.text()) +
                            "&go=&count=10&first=" + str(count))

        return urls

    def findSubdomains(self):
        if self.testWildcard() is True:
            self.textEdit.setText("The target domain has a DNS wildcard configuration.")
        else:
            fileName = self.lineEdit_2.text()
            if fileName:
                # External dictionary
                _file = QFile(fileName)
                if not _file.open(QFile.ReadOnly | QFile.Text):
                    QMessageBox.warning(self, "Error",
                                        "Cannot read file %s.\n%s." % (fileName, _file.errorString()))
                    return

                stream = QTextStream(_file)
                while not stream.atEnd():
                    line = str(stream.readLine())
                    if not line.startswith("#"):
                        subdomain = "%s.%s" % (line.rstrip("\n"), str(self.lineEdit.text()))
                        self.checkHost(subdomain)
            else:
                # Internal dictionary
                for item in database:
                    subdomain = "%s.%s" % (item, str(self.lineEdit.text()))
                    self.checkHost(subdomain)

            if not self.buffer.getvalue():
                self.textEdit.setText("Nothing found.")
            else:
                self.showOutput()

    def findEmails(self):
        results = {}
        urls = self.searchEngine()
        patterns = [re.compile(s) for s in ["[\w\d.-]+@<b>" + str(self.lineEdit_3.text()),
                                            "[\w\d.-]+@<em>" + str(self.lineEdit_3.text()),
                                            "[\w\d.-]+@<strong>" + str(self.lineEdit_3.text())]]

        for url in urls:
            try:
                request = urllib2.Request(url)
                request.add_header("User-agent", random.choice(agents))
                response = urllib2.urlopen(request)
                data = response.read()
                for pattern in patterns:
                    emails = re.findall(pattern, data)
                    for email in emails:
                        cleanEmail = re.sub("<b>|<em>|<strong>", "", email)
                        results[cleanEmail] = 1
            except IOError:
                pass
            except httplib.IncompleteRead:
                QMessageBox.warning(self, "Error", "Error while reading data. Try again.")
                return

        for key in results.keys():
            self.buffer.write(key + "\n")

        if not results:
            self.textEdit.setText("Nothing found.")
        else:
            self.showOutput()

    def findHumanRelationships(self):
        import HTMLParser

        try:
            from BeautifulSoup import BeautifulSoup
        except ImportError:
            QMessageBox.warning(self, "Error",
                                "Please install \'BeautifulSoup\' from http://www.crummy.com/software/BeautifulSoup/.")
            return

        results = {}
        try:
            response = urllib2.urlopen(str(self.lineEdit_4.text()))
        except:
            QMessageBox.warning(self, "Error", "Connection problem. Try again.")
            return

        try:
            rawData = BeautifulSoup(response)
        except HTMLParser.HTMLParseError:
            QMessageBox.warning(self, "Error", "Error while reading data. Try again.")
            return

        data = rawData.findAll("a")
        for item in data:
            for value in xfn:
                if item.has_key("rel") and re.search(value, item["rel"]) is not None:
                    results[item.string] = item["href"], item["rel"]

        for key, values in results.items():
            self.buffer.write("NAME :  " + key)
            self.buffer.write("\nURL :  " + values[0])
            self.buffer.write("\nRELATIONSHIP :  " + re.sub(" ", ", ", values[1]) + "\n\n")

        if not results:
            self.textEdit.setText("Nothing found.")
        else:
            self.showOutput()

    def zoneTransfer(self):
        try:
            import dns.resolver
            import dns.query
            import dns.zone
        except ImportError:
            QMessageBox.warning(self, "Error", "Please install \'dnspython\' from http://www.dnspython.org/.")
            return

        results = []
        NS = []
        try:
            servers = dns.resolver.query(str(self.lineEdit_5.text()), "NS")
        except dns.resolver.NXDOMAIN:
            QMessageBox.warning(self, "Error", "Non-Existent Domain response.")
            return

        for server in servers:
            NS.append(str(server))

        for target in NS:
            try:
                zoneTransfer = dns.zone.from_xfr(dns.query.xfr(target.rstrip("."), str(self.lineEdit_5.text())))
                names = zoneTransfer.nodes.keys()
                names.sort()
                self.buffer.write("=-=-=-   SERVER: " + target.rstrip(".") + "\n\n")
                for name in names:
                    results.append(zoneTransfer[name].to_text(name))
                    self.buffer.write(re.sub(" ", "   ", zoneTransfer[name].to_text(name)) + "\n")

                self.buffer.write("\n")
            except:
                pass

        if not results:
            self.textEdit.setText("Zone transfer is not possible.")
        else:
            self.showOutput()

    def checkShodan(self, key):
        try:
            from shodan import WebAPI
        except ImportError:
            QMessageBox.warning(self, "Error",
                                "Please install \'shodan-python\' from https://github.com/achillean/shodan-python/.")
            return

        try:
            api = WebAPI(key)
            results = api.host(str(self.lineEdit_6.text()))
            self.buffer.write("=-=-=-   GENERAL INFO:\n\nIP: " + results["ip"] +
                              "\nCountry: " + results.get("country_name", "None") +
                              "\nCity: " + results.get("city", "None") +
                              "\n\n=-=-=-   ALL BANNERS:\n\n")

            for item in results["data"]:
                self.buffer.write("Port: " + str(item["port"]) + "\n" + item["banner"])
        except Exception, err:
            if str(err) == "No information available for that IP.":
                self.textEdit.setText("No information available for that IP.")
            else:
                QMessageBox.warning(self, "Error", "%s." % err)

            return

        self.showOutput()

    def showOutput(self):
        self.textEdit.setText(self.buffer.getvalue())
        self.buffer.truncate(0)
        self.buffer.seek(0)

    def exitApplication(self):
        self.writeSettings()
        self.close()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = QuickRecon()
    mainWindow.show()
    sys.exit(application.exec_())

