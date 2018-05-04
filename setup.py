from setuptools import setup

setup(name='negspy',
      version='0.2.20',
      description='Python NGS tools',
      author='Peter Kerpedjiev',
      author_email='pkerpedjiev@gmail.com',
      url='',
      packages=['negspy'],
      package_data={'negspy': ['data/*/chromInfo.txt', 'data/*/chromOrder.txt']},
      scripts=['scripts/chr_pos_to_genome_pos.py', 'scripts/make_triangular.py', 'scripts/create_chrominfo.py']

     )
