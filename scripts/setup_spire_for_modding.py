import os
import shutil

def main():
    # Make the build directory
    project_root = os.path.dirname(os.path.dirname(__file__))
    build_dir = os.path.join(project_root, 'build')

    os.makedirs(os.path.join(build_dir, 'mods'))

    # TODO: Handle other steam installs, allow user to define steam base dir
    slay_the_spire_dir = os.path.join(
        os.environ['HOME'],
        '.steam',
        'steam',
        'steamapps',
        'common',
        'SlayTheSpire',
    )

    slay_the_spire_file = 'desktop-1.0.jar'
    shutil.copy(
        os.path.join(slay_the_spire_dir, slay_the_spire_file),
        os.path.join(build_dir, slay_the_spire_file),
    )

    if not os.path.exists(os.path.join(build_dir, 'jre')):
        shutil.copytree(
            os.path.join(slay_the_spire_dir, 'jre'),
            os.path.join(build_dir, 'jre'),
        )

if __name__ == '__main__':
    main()

