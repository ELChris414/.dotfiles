from .default import DefaultColor

class Color(DefaultColor):
    USERNAME_FG = 15
    USERNAME_BG = 34
    USERNAME_ROOT_BG = 160

    HOSTNAME_FG = 15
    HOSTNAME_BG = 20

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 33
    HOME_FG = 15
    PATH_BG = 117
    PATH_FG = 16
    CWD_FG = 17
    SEPARATOR_FG = 17

    READONLY_BG = 160
    READONLY_FG = 15

    SSH_BG = 166
    SSH_FG = 254

    REPO_CLEAN_BG = 148
    REPO_CLEAN_FG = 0
    REPO_DIRTY_BG = 161
    REPO_DIRTY_FG = 15

    JOBS_FG = 39
    JOBS_BG = 238

    CMD_PASSED_BG = 236
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 161
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22

    GIT_AHEAD_BG = 240
    GIT_AHEAD_FG = 250
    GIT_BEHIND_BG = 240
    GIT_BEHIND_FG = 250
    GIT_STAGED_BG = 22
    GIT_STAGED_FG = 15
    GIT_NOTSTAGED_BG = 130
    GIT_NOTSTAGED_FG = 15
    GIT_UNTRACKED_BG = 52
    GIT_UNTRACKED_FG = 15
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = 15

    VIRTUAL_ENV_BG = 35
    VIRTUAL_ENV_FG = 00
