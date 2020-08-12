echo ---- CR2 Engineer Logger ----
echo Written by: Jonah Hendler
echo -----------------------------

sudo python -m smtpd -c DebuggingServer -n localhost:1025 &
python input_box.py

echo ---- Closing CR2 Logger ----
