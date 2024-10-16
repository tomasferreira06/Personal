# Package Management

<mark style="color:red;">**Debian/Ubuntu (APT):**</mark>

* <mark style="color:yellow;">**apt-get install \[package]**</mark>**:** Installs a package.
  * Example: <mark style="color:blue;">`apt-get install nginx`</mark>
* <mark style="color:yellow;">**apt-get remove \[package]**</mark>**:** Uninstalls a package.
  * Example: <mark style="color:blue;">`apt-get remove nginx`</mark>
* <mark style="color:yellow;">**apt-get update**</mark>**:** Updates the package list.
* <mark style="color:yellow;">**apt-get upgrade**</mark>**:** Upgrades installed packages.

<mark style="color:red;">**Red Hat/CentOS (YUM/DNF):**</mark>

* <mark style="color:yellow;">**yum install \[package]**</mark>**:** Installs a package.
  * Example: <mark style="color:blue;">`yum install httpd`</mark>
* <mark style="color:yellow;">**yum remove \[package]**</mark>**:** Uninstalls a package.
  * Example: <mark style="color:blue;">`yum remove httpd`</mark>
* <mark style="color:yellow;">**yum update**</mark>**:** Updates installed packages.
* <mark style="color:yellow;">**dnf install \[package]**</mark>**:** (Alternative to <mark style="color:blue;">yum</mark> on newer systems)

<mark style="color:red;">**Arch Linux (Pacman):**</mark>

* <mark style="color:yellow;">**pacman -S \[package]**</mark>**:** Installs a package.
  * Example: <mark style="color:blue;">`pacman -S vim`</mark>
* <mark style="color:yellow;">**pacman -R \[package]**</mark>**:** Uninstalls a package.
  * Example: <mark style="color:blue;">`pacman -R vim`</mark>
* <mark style="color:yellow;">**pacman -Syu**</mark>**:** Updates the package database and upgrades all installed packages.

<mark style="color:red;">**Generic Package Management:**</mark>

* <mark style="color:yellow;">**dpkg -i \[package.deb]**</mark>**:** Installs a Debian package.
  * Example: <mark style="color:blue;">`dpkg -i package.deb`</mark>
* <mark style="color:yellow;">**dpkg -r \[package]**</mark>**:** Removes a Debian package.
  * Example: <mark style="color:blue;">`dpkg -r nginx`</mark>
* <mark style="color:yellow;">**dpkg -l**</mark>**:** Lists installed packages.

<mark style="color:red;">**RPM Package Management:**</mark>

* <mark style="color:yellow;">**rpm -ivh \[package.rpm]**</mark>**:** Installs an RPM package.
  * Example: <mark style="color:blue;">`rpm -ivh package.rpm`</mark>
* <mark style="color:yellow;">**rpm -e \[package]**</mark>**:** Uninstalls an RPM package.
  * Example: <mark style="color:blue;">`rpm -e httpd`</mark>
* <mark style="color:yellow;">**rpm -qa**</mark>**:** Lists all installed RPM packages.

<mark style="color:red;">**Snap (Snapcraft):**</mark>

* <mark style="color:yellow;">**snap install \[package]**</mark>**:** Installs a Snap package.
  * Example: <mark style="color:blue;">`snap install vscode`</mark>
* <mark style="color:yellow;">**snap remove \[package]**</mark>**:** Removes a Snap package.
  * Example: <mark style="color:blue;">`snap remove vscode`</mark>
* <mark style="color:yellow;">**snap list**</mark>**:** Lists installed Snap packages.

<mark style="color:red;">**Flatpak:**</mark>

* <mark style="color:yellow;">**flatpak install \[package]**</mark>**:** Installs a Flatpak package.
  * Example: <mark style="color:blue;">`flatpak install org.gimp.GIMP`</mark>
* <mark style="color:yellow;">**flatpak uninstall \[package]**</mark>**:** Uninstalls a Flatpak package.
  * Example: <mark style="color:blue;">`flatpak uninstall org.gimp.GIMP`</mark>
* <mark style="color:yellow;">**flatpak list**</mark>**:** Lists installed Flatpak packages.

These commands are essential for managing software packages on various Linux distributions.&#x20;

Choose the appropriate set of commands based on your system's package manager.
