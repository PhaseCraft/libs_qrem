import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        "libs_qrem",
        sources=[
            "./libs_qrem/libs_qrem.pyx",
            "./cpp/eigen_utils.cpp",
            "./cpp/combinations.cpp",
            "./cpp/hamming.cpp",
            "./cpp/sgs_algorithm.cpp",
            "./cpp/harger_higham.cpp",
            "./cpp/qrem_filter.cpp",
            "./cpp/ignis_filter.cpp",
            "./cpp/delta_filter.cpp",
            "./cpp/least_norm_filter.cpp",
            "./cpp/mooney_etal_filter.cpp",
            "./cpp/nation_etal_filter.cpp",
        ],
        extra_compile_args=["-std=c++17", "-pthread"],
        include_dirs=["./eigen"],
        language="c++",
    ),
]

setup(
    name="libs_qrem",
    description="efficient quantum readout error mitigation library",
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(ext_modules, language_level=3),
    include_dirs=[np.get_include()],
    zip_safe=False,
    packages=["libs_qrem"],
    package_dir={"libs_qrem": "libs_qrem"},
)
