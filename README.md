<img alt="dysonMacOS Logo" src="https://github.com/fhenwood/dysonMacOS/blob/main/data/app_icon.png" width="250" />

# dysonMacOS
A menu bar app for Mac OS which allows you to remotely control your Dyson AM09 (without the remote control) - using a Broadlink RM IR Blaster. Built using rumps.

<img width="250" alt="Dyson Fan Controller Screenshot" src="https://user-images.githubusercontent.com/52894937/165625848-f0a3f744-8ea9-4f0d-a06a-5c163130469f.png">

## 📦 Installation
1. Setup your Broadlink RM on your local network.
2. Ensure you have the dependencies installed
```
pip install broadlink py2app rumps cffi
```
3. Clone the dysonMacOS Repo and use py2app to comply.
```
git clone https://github.com/fhenwood/dysonMacOS.git
cd dysonMacOS
python setup.py py2app
```
4. Copy the .app file from the dysonMacOS folder to your Applications.
5. Bingo, enjoy!

## 💡 Features
- Set temperatures and fan speed without knowing the current state of the fan!
- Turn on and off.
- Switch between hot and cold.
- Spin.
- Displays fan temperature when known.
- Reset current state to an known state if out of sync due to changes via an external remote control.

## 🔨 Contributor 
Feel free to create pull requests. Feel free to add more dyson fans via learning the IR codes:
```
broadlink.discover()
```
Please encode the byte IR codes into base64 str, and store in a json.
