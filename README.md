<div align="center">

# Установка Arch Linux
https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db

<br>

# Скриншот
![screenshot](./assets/screenshot.png)

# Установка для Arch Linux
</div>

## Установка Xserver
```
sudo pacman -S xorg-server xorg-apps xorg-xinit
```

## Установка i3-gaps
```
sudo pacman -S i3-gaps polybar rofi
```

## Установка lightdm (окно для входа в систему), если вам не нужен - пропускайте
```
sudo pacman -S lighdm lightdm-gtk-greeter
```
```
sudo systemctl enable lighdm
```

## Скопируем конфиги и обои
```
cd Documents
```
```
git clone https://github.com/MihailMuh/i3-gaps-config.git
```
```
cd i3-gaps-config
```
```
cp -r ./config/* ~/.config
```
```
cp -r ./wallpapers ~/Pictures/
```
```
sudo cp ./wallpapers/space.jpg /usr/share/pixmaps/
```
```
sudo chmod u+x ~/.config/polybar/launch.sh
```

### Установка терминала, файлового менеджера, менеджера обоев, менеджера анимаций, менеджера скриншотов, шрифта с поддержкой иконок, аудиоплеера (соответсвенно)
```
sudo pacman -S alacritty thunar nitrogen picom gnome-screenshot ttf-font-awesome vlc
```
Для настройки своих обоев пишите в терминал ```nitrogen```

## Установка PulseAudio
```
sudo pacman -S pulseaudio pulseaudio-alsa
```

## Установка paru (для гугла и не только)
```
git clone https://aur.archlinux.org/paru.git
```
```
cd paru
```
```
makepkg -si
```

### Установка гугла, текстового редактора, графического менеджера wifi сетей, календарика, просмотрщика изображений и плагин для .webp, диспетчера задач, пакета оффис, шрифты для оффиса (соответсвенно)
```
paru -S google-chrome sublime-text-3 networkmanager-dmenu zenity qview qt5-imageformats gnome-system-monitor wps-office ttf-wps-fonts ttf-ms-fonts
```

Символическая ссылка, чтобы открывать sublime через консоль, например ```subl /etc/hosts```
```
sudo ln -s /opt/sublime_text_3/sublime_text /usr/local/bin/subl
```

## Настройка обоев для lightdm
```
paru -S lightdm-gtk-greeter-settings
```
```
sudo subl /etc/lightdm/lightdm-gtk-greeter.conf
```
В конце файла находим блок ```[greeter]``` и вместо ```#background=``` пишем ```background=/usr/share/pixmaps/space.jpg```

## Изменение яркости
По умолчанию, Linux ограничивает возможность изменения яркости. Чтобы это обойти, необходимо добавить пользователя в группу ```video```
```
sudo usermod -a -G video you_username
```
И в файл
```
sudo subl /etc/udev/rules.d/backlight.rules
```
Добавить правило
```
ACTION=="add", SUBSYSTEM=="backlight", RUN+="/bin/chgrp video $sys$devpath/brightness", RUN+="/bin/chmod g+w $sys$devpath/brightness"
```

## Перезагрузка
```
sudo reboot
```
