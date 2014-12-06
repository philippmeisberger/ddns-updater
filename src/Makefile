BINDIR = $(DESTDIR)/usr/sbin

clean:
	rm -f *.py[co] */*.py[co]

install:
	mkdir -p $(DESTDIR)/etc/ddns-updater/
	cp -r files/etc/ $(DESTDIR)/
	cp -r files/usr/ $(DESTDIR)/

uninstall:
	rm -f $(DESTDIR)/etc/cron.d/ddns-updater
	rm -rf $(DESTDIR)/etc/ddns-updater/
	rm -f $(BINDIR)/ddns-updater
