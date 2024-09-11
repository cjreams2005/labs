{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c8a971f8-da3a-4e22-af23-5208ffa2b001",
   "metadata": {},
   "source": [
    "Problem 3: Unit Convertor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "da83bdc3-5c60-4781-9687-cb25f20501e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please input the number (with units) you wish to convert:  44 in\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44 in = 111.76 cm\n"
     ]
    }
   ],
   "source": [
    "start = input(\"Please input the number (with units) you wish to convert: \")\n",
    "changed = start\n",
    "if \"in\" in start:\n",
    "    changed = changed.strip(\" in\")\n",
    "    changed = float(changed)\n",
    "    changed = changed*2.54\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" cm\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"cm\" in start:\n",
    "    changed = changed.strip(\" cm\")\n",
    "    changed = float(changed)\n",
    "    changed = changed/2.54\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" in\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"yd\" in start:\n",
    "    changed = changed.strip(\" yd\")\n",
    "    changed = float(changed)\n",
    "    changed = changed*0.9144\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" m\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"m\" in start:\n",
    "    changed = changed.strip(\" m\")\n",
    "    changed = float(changed)\n",
    "    changed = changed/0.9144\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" yd\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"lb\" in start:\n",
    "    changed = changed.strip(\" lb\")\n",
    "    changed = float(changed)\n",
    "    changed = changed*0.45359237\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" kg\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"kg\" in start:\n",
    "    changed = changed.strip(\" kg\")\n",
    "    changed = float(changed)\n",
    "    changed = changed/0.45359237\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" lb\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"oz\" in start:\n",
    "    changed = changed.strip(\" oz\")\n",
    "    changed = float(changed)\n",
    "    changed = changed*28.349523125\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" g\"\n",
    "    print(f\"{start} = {changed}\")\n",
    "elif \"g\" in start:\n",
    "    changed = changed.strip(\" g\")\n",
    "    changed = float(changed)\n",
    "    changed = changed/28.349523125\n",
    "    changed = round(changed,2)\n",
    "    changed = str(changed)\n",
    "    changed = changed + \" oz\"\n",
    "    print(f\"{start} = {changed}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e2134af-803d-4c99-92b1-729255f5d49e",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "122931ec-1725-4f36-9049-6caed8ebac22",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
