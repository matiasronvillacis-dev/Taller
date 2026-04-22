{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/matiasronvillacis-dev/Taller/blob/main/Estudiante.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Taller en clase, Realizar clase estudiante con objetos y atributos, la cedula solo tiene valores numericos y a 10 digitos y el semestre solo permite del 1 al 9"
      ],
      "metadata": {
        "id": "DMsSOn3Y-iKP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Estudiante:\n",
        "    \"\"\"Clase que representa a un estudiante con validaciones estrictas.\"\"\"\n",
        "\n",
        "    def __init__(self, nombre, apellido, cedula, email, semestre):\n",
        "        self.nombre = nombre\n",
        "        self.apellido = apellido\n",
        "        # Los siguientes activan los setters para validación inicial\n",
        "        self.cedula = cedula\n",
        "        self.email = email\n",
        "        self.semestre = semestre\n",
        "        self.__materias = []  # Atributo privado\n",
        "\n",
        "    # --- Propiedad: Cédula (Encapsulada) ---\n",
        "    @property\n",
        "    def cedula(self):\n",
        "        return self.__cedula\n",
        "\n",
        "    @cedula.setter\n",
        "    def cedula(self, valor):\n",
        "        if isinstance(valor, str) and valor.isdigit() and len(valor) == 10:\n",
        "            self.__cedula = valor\n",
        "        else:\n",
        "            raise ValueError(\"Error: La cédula debe tener 10 dígitos numéricos.\")\n",
        "\n",
        "    # --- Propiedad: Semestre (Encapsulada) ---\n",
        "    @property\n",
        "    def semestre(self):\n",
        "        return self.__semestre\n",
        "\n",
        "    @semestre.setter\n",
        "    def semestre(self, valor):\n",
        "        if isinstance(valor, int) and 1 <= valor <= 9:\n",
        "            self.__semestre = valor\n",
        "        else:\n",
        "            raise ValueError(\"Error: El semestre debe ser un entero entre 1 y 9.\")\n",
        "\n",
        "    # --- Gestión de Materias (Lógica de Negocio) ---\n",
        "    @property\n",
        "    def materias(self):\n",
        "        \"\"\"Retorna una copia de la lista para proteger la original.\"\"\"\n",
        "        return self.__materias.copy()\n",
        "\n",
        "    def agregar_materia(self, materia):\n",
        "        \"\"\"Método público para modificar el atributo privado __materias.\"\"\"\n",
        "        if materia and isinstance(materia, str):\n",
        "            self.__materias.append(materia.strip())\n",
        "\n",
        "    def __str__(self):\n",
        "        \"\"\"Representación formal del objeto siguiendo PEP 8.\"\"\"\n",
        "        return (f\"Estudiante: {self.nombre} {self.apellido} | \"\n",
        "                f\"ID: {self.cedula} | Semestre: {self.semestre}\")\n",
        "\n",
        "\n",
        "# --- Bloque de ejecución ---\n",
        "if __name__ == \"__main__\":\n",
        "    try:\n",
        "        # Instanciación correcta\n",
        "        estudiante_uno = Estudiante(\n",
        "            \"Luis\", \"Ramírez\", \"0987654321\", \"luis@correo.com\", 4\n",
        "        )\n",
        "        estudiante_uno.agregar_materia(\"Cálculo Integral\")\n",
        "\n",
        "        print(estudiante_uno)\n",
        "        print(f\"Materias inscritas: {estudiante_uno.materias}\")\n",
        "\n",
        "        # Intento de acceso directo al atributo privado (lanzará error si se intenta)\n",
        "        # print(estudiante_uno.__cedula)  # Esto daría AttributeError\n",
        "\n",
        "    except ValueError as e:\n",
        "        print(f\"Validación fallida: {e}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JwACtZ5LA9hY",
        "outputId": "b200b989-fb97-4929-d6b5-504a2e86f340"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Estudiante: Luis Ramírez | ID: 0987654321 | Semestre: 4\n",
            "Materias inscritas: ['Cálculo Integral']\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Te damos la bienvenida a Colaboratory",
      "toc_visible": true,
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}