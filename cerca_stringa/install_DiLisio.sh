mkdir $HOME/esercitazione
cp requirements.txt ./esercitazione
cp script.py ./esercitazione
cd esercitazione
virtualenv myenv
source myenv/bin/activate
pip3 install -r requirments.txt
