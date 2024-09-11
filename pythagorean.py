{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b5f11c94-e7c5-43be-b1e0-6e687dba0584",
   "metadata": {},
   "source": [
    "Problem 1: Solve Pythagorean theorem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cf744b7e-7601-46bb-84b1-ebcceba59b3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is the length of the first side?:  4\n",
      "What is the length of the second side?:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The hypotenuse is 8.06.\n"
     ]
    }
   ],
   "source": [
    "side_one = float(input(\"What is the length of the first side?: \"))\n",
    "side_two = float(input(\"What is the length of the second side?: \"))\n",
    "hypotenuse = ((side_one**2)+(side_two**2))**0.5\n",
    "hypotenuse = round(hypotenuse, 2)\n",
    "print(f\"The hypotenuse is {hypotenuse }.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dce2fdcd-b97b-4db5-8009-88e41ddf1c34",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edfbde55-b938-49fe-89b4-361b95f55ad3",
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
