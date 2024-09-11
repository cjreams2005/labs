{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "23440da4-76ad-49cc-9d69-2993510877b1",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "935f7077-97b0-43b2-97b3-9a00f2dba0f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please input the radius of the circle:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n",
      "The circle with radius 10.0 has an area of 314.16 and a perimeter of 62.83.\n"
     ]
    }
   ],
   "source": [
    "radius = float(input(\"Please input the radius of the circle: \"))\n",
    "import math\n",
    "pi_value = math.pi\n",
    "print(pi_value)\n",
    "area = (radius**2)*(pi_value)\n",
    "area = round(area, 2)\n",
    "parimeter = 2*radius*pi_value\n",
    "parimeter = round(parimeter, 2)\n",
    "print(f\"The circle with radius {radius} has an area of {area} and a perimeter of {parimeter}.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2905f741-6381-4e52-bbc1-01d045f8965a",
   "metadata": {},
   "source": [
    "---"
   ]
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
